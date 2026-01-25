function pmApp() {
    return {
        loading: true,
        activeTab: 'tasks',

        people: [],
        projects: [],
        tasks: [],

        taskStatuses: ['Todo', 'In Progress', 'Blocked', 'Done'],
        projectStatuses: ['Backlog', 'Active', 'On Hold', 'Done'],
        personRoles: ['Lead', 'Partner', 'Network', 'Client'],

        filters: {
            person: '',
            project: ''
        },

        toast: {
            show: false,
            message: ''
        },

        sortableInstances: [],

        async init() {
            await this.loadData();
            this.$nextTick(() => {
                this.initSortable();
            });

            // Re-init sortable when tab changes
            this.$watch('activeTab', () => {
                this.$nextTick(() => {
                    this.initSortable();
                });
            });
        },

        async loadData() {
            this.loading = true;
            try {
                const response = await fetch('/api/all');
                const data = await response.json();
                this.people = data.people;
                this.projects = data.projects;
                this.tasks = data.tasks;
            } catch (error) {
                console.error('Failed to load data:', error);
                this.showToast('Failed to load data');
            }
            this.loading = false;
        },

        get filteredTasks() {
            let result = this.tasks;

            if (this.filters.person) {
                result = result.filter(task => {
                    const person = this.getPersonFromTask(task);
                    return person && person.includes(this.filters.person);
                });
            }

            if (this.filters.project) {
                result = result.filter(task => {
                    const project = this.getProjectFromTask(task);
                    return project && project.includes(this.filters.project);
                });
            }

            return result;
        },

        getPersonFromTask(task) {
            const person = task.metadata.person;
            if (!person) return null;
            const match = person.match(/\[\[([^\]]+)\]\]/);
            if (match) {
                return match[1].replace('Person - ', '');
            }
            return person;
        },

        getProjectFromTask(task) {
            const project = task.metadata.project;
            if (!project) return null;
            const match = project.match(/\[\[([^\]]+)\]\]/);
            if (match) {
                return match[1].replace('Project - ', '');
            }
            return project;
        },

        getPersonFromProject(project) {
            const person = project.metadata.person;
            if (!person) return null;
            const match = person.match(/\[\[([^\]]+)\]\]/);
            if (match) {
                return match[1].replace('Person - ', '');
            }
            return person;
        },

        initSortable() {
            // Destroy existing instances
            this.sortableInstances.forEach(s => s.destroy());
            this.sortableInstances = [];

            // Task columns
            if (this.activeTab === 'tasks') {
                document.querySelectorAll('.task-column').forEach(column => {
                    const sortable = new Sortable(column, {
                        group: 'tasks',
                        animation: 150,
                        ghostClass: 'sortable-ghost',
                        dragClass: 'sortable-drag',
                        onEnd: async (evt) => {
                            const taskId = evt.item.dataset.id;
                            const newStatus = evt.to.dataset.status;
                            await this.updateTaskStatus(taskId, newStatus);
                        }
                    });
                    this.sortableInstances.push(sortable);
                });
            }

            // Project columns
            if (this.activeTab === 'projects') {
                document.querySelectorAll('.project-column').forEach(column => {
                    const sortable = new Sortable(column, {
                        group: 'projects',
                        animation: 150,
                        ghostClass: 'sortable-ghost',
                        dragClass: 'sortable-drag',
                        onEnd: async (evt) => {
                            const projectId = evt.item.dataset.id;
                            const newStatus = evt.to.dataset.status;
                            await this.updateProjectStatus(projectId, newStatus);
                        }
                    });
                    this.sortableInstances.push(sortable);
                });
            }
        },

        async updateTaskStatus(taskId, newStatus) {
            try {
                const response = await fetch(`/api/tasks/${taskId}`, {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ status: newStatus })
                });

                if (response.ok) {
                    // Update local state
                    const task = this.tasks.find(t => t.id === taskId);
                    if (task) {
                        task.status = newStatus;
                    }
                    this.showToast(`Task moved to ${newStatus}`);
                } else {
                    this.showToast('Failed to update task');
                    await this.loadData(); // Reload to sync
                }
            } catch (error) {
                console.error('Failed to update task:', error);
                this.showToast('Failed to update task');
                await this.loadData();
            }
        },

        async updateProjectStatus(projectId, newStatus) {
            try {
                const response = await fetch(`/api/projects/${projectId}`, {
                    method: 'PATCH',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ status: newStatus })
                });

                if (response.ok) {
                    const project = this.projects.find(p => p.id === projectId);
                    if (project) {
                        project.status = newStatus;
                    }
                    this.showToast(`Project moved to ${newStatus}`);
                } else {
                    this.showToast('Failed to update project');
                    await this.loadData();
                }
            } catch (error) {
                console.error('Failed to update project:', error);
                this.showToast('Failed to update project');
                await this.loadData();
            }
        },

        copyPath(path) {
            navigator.clipboard.writeText(path).then(() => {
                this.showToast(`Copied: ${path}`);
            }).catch(() => {
                this.showToast('Failed to copy path');
            });
        },

        showToast(message) {
            this.toast.message = message;
            this.toast.show = true;
            setTimeout(() => {
                this.toast.show = false;
            }, 2000);
        }
    };
}
