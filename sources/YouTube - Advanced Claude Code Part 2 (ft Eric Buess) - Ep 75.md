# Advanced Claude Code Part 2 (ft Eric Buess) - Ep 75

**Source**: https://www.youtube.com/watch?v=8jAJIq6-M_Q
**Channel**: Tool Use - AI Conversations
**Date Retrieved**: 2026-01-22

---

## Transcript

Is Claude code the everything agent? Back on episode 52, Eric Boost taught us about advanced Cloud Code usage. Well,
on episode 75, Eric's back and he's been building non-stop since we saw him last. And today, we're going to cover how Eric
has built a system that allows him to control Cloud Code from anywhere, be confident that the task will be done
correctly, interact with so many aspects of his life, and much more. So, please enjoy this conversation with Eric Boo.
So if you can have control over the terminal, then that means that the whole there's not really any limits. And so if
AI is the abstraction and it's just you're talking in in English to the the computer that has full control over it,
then you're not really boxed in. So that you can set up permission structures and sandboxes and things like that, but it's
not required. And so one thing about cloud code that's so awesome is they have not only are they dog fooding it
internally inside of enthropic which means that they're using the tool to build the tool the new releases 100% of
the releases are written by cloud code because it's got become so reliable and so good and you could see that number
increasing over the last you know few months and now it's entirely like super fast building and deploying new things
and so they're they're iterating with cloud code and they're releasing the things that they find internally that
work I um purpose-built for their model. Their model is trained to do better at cloud code. And so it's not like some
other system that you're sort of using to bootstrap the or so be a harness or whatever like a a wrapper around um the
the model itself. It's something that the team inside the company that builds the model is doing. It's like a vertical
stack, right? And so you can imagine that OpenAI is doing this with codecs and Google with jewels or like whatever
their tools are that they're releasing anti-gravity and stuff like that and grock has their own. Anyway, with
anthropic I personally believe it was just the best coding model. Now it has a limitation that it has like a smaller
context window than some of the others but you know for instruction following from most of the stuff that you do
agentically in the terminal um you don't really need all that much. Um, and in fact, the ability for the model to do
really good task work cuts down if you even if you have a really large car context window on it, but it's not
following instructions all that well over time when it fills up. Um, that's, you know, you just have to test each
model, right? So, they're all really good. They're all really capable, but the thing about Enthropics Cloud Code is
that they have this hook system. And I feel like this is essential. Like this is the gold standard. I thought cloud
code is the gold standard for coding because of uh not only this like internal rapid development and they're
releasing it to you and not only because you have something like in the cloud desktop app you can now do cloud code in
the browser you can do cloud code you can access it from like GitHub you can access this if you have if you have the
pro plan even the $20 month plan you can get access to all this stuff but if you have the max plan you can get the
preview things like the new things that come out and including like co-work which was just released in in cloud
desktop and and that relies on cloud code under the hood the hook system is actually available in all those things.
I didn't know when we talked yesterday, but I took a look and it's it's there. It's just kind of limited because it's
somewhat in like the sandbox VM and it's you got to get stuff out the hooks out and back in. But here's why the hooks
matter. So, with every uh aentic tool you might use that you want to have do something on your behalf. Um there are
some limitations. There's some uh constraints or or things it does that aren't quite right. Like ideally, let's
set the the stage. Here's what you want. You want to be able to talk to it like you talk to a human, like someone who's
a project manager or let's say Jarvis, your Iron Man's AI or your secretary or personal assistant because the goal is
for me in my life, I want to be able to get back more times that are meaningful with the people and the relationships
and like what I care about is more meaningful. So just imagine for a moment all the things that you do in life in
personal and work life. I don't know can't say over here so I'm counting. Um, and like if you were to rank order those
things by like these are the the sets of tasks or subtasks that I do that I really like and these are the ones I
like less, right? They're kind of more automated or mundane or automatable, I would say, like repetitive and mundane
and I wish I didn't have to do so much of this set of tasks. I could do more. Well, of this set of tasks is lower.
There's a subset of those. There's like a like some of those tasks that you could probably automate away with AI if
you knew how to do it. And and it's the models are like as many people said like the worse they're ever going to be.
They're just getting better. And the sooner you get in at learning how to use the tools to to take over whatever it is
that you don't want to do, the more uh ahead of the curve you are and the better you are at getting back more of
that time. And it's a flywheel. It's a feedback loop, right? So like once you learn how to do it for here for this
thing that you're super passionate about, be like it would be really great if I could just not have to do that
anymore. then that skill up of investing the time to work with the model to do that uh allows you to do a lot more and
I have a I feel like a compelling reason for me to say that the place to start with that or if you've already done it
to try is uh claude code now there's different ways to use it again you can use it in the the desktop app you can
use it in the website you can use it in the terminal a lot of people are too intimidated by the terminal to get into
it and it is like superpower lands so um you can start wherever you want to start I personally would start this terminal
but because that is the the place where there are no limits. Um but anyway like the goal being I want to find one thing
that I don't want to do anymore but I want to find a tool that can automate it so I don't have to do that anymore. Uh
and if that thing is like doing this document work okay and you have a max subscription or you're willing to pay
for it. That's $100 a month for the 5x and and 200 for the 20x and that's 20x of what you get in the pro plan which is
$20 a month. I think that that's right. Not sure. But u which is the pro plan you get more than the free plan. Anyway,
it's if the pro plan I think is $20 a month. I'm not working for Antropic. I don't sell this stuff. I don't really
know. But I think that if you if you get one of the Mac subscriptions, you can use co-work. Of course, co-work will
probably come to the the pro subscription pretty soon. But um that's for like cloud code except it's not code
uh related. It's more like general purpose. I have these documents. I want to create this presentation. I it you
know a lot of things can do that. You think, well, that's not special. Any AI can turn documents into a presentation.
But it's different. There's much more that you can do. Okay? [snorts] Like cloud code is another tab inside of
cloud desktop app. And with cloud code in that tab, uh you can basically connect it to your GitHub or your local
file system and it can work within the sandbox of whatever you set up and it can create a little VM. It can do stuff
uh on your computer writing your actual code files. And this is what matters versus a lot of the other systems that
you'll see. The state that's being managed is your local code, your local files, your local documents and it can
copy it out of there and put it into its little sandbox environment or you can give it access to whatever folder you
want. And um there's a lot of things that it can do and depending on like there's even a file system tool I can
show you a lot of this stuff. I don't know how much we'll get into but I would love to like walk people through at some
point but cloud code in the terminal has everything. And so here's here's where I'm going with it. So, I wanted
personally, well, the thing that I said that I want is I am overwhelmed. I have four kids between the ages of 15 and
six. And I have one that's due in a month. So, in baby number five. Uh, and we're very excited about that, but
there's far too many school emails, okay, from the teachers, especially ones in high school and middle school. And
there's far too much to keep up with. I've got calendar events like crazy. I've got text messages and Teams and
Group Me and emails and all the things that everyone else struggles with, right? How do you keep up with all this
stuff? So, I wanted a system to keep up with all that stuff. Well, I wanted to build something like Jarvis that is a
secretary or the front end that can look at all the data coming in from all the sources without me having to open any
website or app ever except for my daily to-do list that is automatically managed based on what it knows that I need and
my calendar which has automatically been scheduled based on events that come in or newsletters or stuff that matters to
me. and it I can identify like this is for you know here's a bunch of stuff coming up but is it relevant to me do I
need to know it or is it just like your your kid is learning to color on today or is it like there's this event that's
coming up and I they need to have this and I need to like RSVP so those are the things that are different right and then
also like text messages and not only do I need to be able to know about this stuff I want to coate together
intelligently by a model such that if it decides here's an important thing it can put it on my calendar but can also
update the calendar. If I get a text that's different, that's for the same event, for the same person, it can like
fill update the content from it, right? I've built that system and it's very simple. I didn't write any code. I won't
say super simple, like I had to struggle with it a little bit, but that system now exists so I can keep up and not be
drowned and not miss things and actually be the dad who knows about where my kids events are, right? And I said it a lot
because I like, okay, I want to do this now. I want to do that next thing and then the next thing once you learn to do
the first thing that's the biggest curve and then you you keep going and there's a little bit more. So within this the
struggle is largely like what is the model doing wrong and how do how do I get the model to be um better at not
going off the rails in this crazy way every time like it's just if it fails it's typ like some default behavior in
the model and how do I get it to not do that? This is where I think the massive value in the hook system lies is because
I mentioned this in the last podcast that we did, but like hooks run outside of the awareness of the model. The model
that you're talking to being like for me claude opus 4.5 within the terminal within cloud code, but outside of that
in the life cycle of the model run, there's there's a bunch of events that are occurring. So when the user sends a
message to the model, there's something called a like a a user prompt hook and or user submit hook. I forget the name
of the hoop honestly but but like at that moment before it sends that message to the model it can be intercepted by
some code which is this hook call and so the hook call that each one of these stages like before it returns back to
the user when it's about to write files when it's about to read file about to call a tool it's about to compact um
before it does any of these things you have an opportunity to guide it or direct it or inject content into it and
so instead of what most people do and how cloud code by default is set up is they just use the the default harness
the default way that cloud is uh intended to be used but without taking advantage of a lot of the there's I
would say there's a lot of optimization that's left on the table and cloud code is much uh more capable than most of
these agentic tools but it's still hobbled quite a bit by uh the defaults and the team the cloud code team at
anthropic I know is working to like make it better and better and they're going to integrate a bunch of this stuff but
what I found is if you have something called a cloud.md file which is a file that contains instructions or contents
that you put in there or that it it decides based on what you tell it to to put in there and when it starts a
session it reads that file. The problem is that as your conversation with the model to build or do something for you
gets longer and longer, it starts to ignore more and more of that that cloud file because it's it's older and you got
re recent user messages and you've got tools, you got all these things that happen. And so you it's not 100%
reliable. And so the goal is how do you get something such that when you give it a task like a human, it's going to know
where to break down all the pieces of the task and when what project to put it in and how to queue it up and where to
slot all those task areas and what to do first, what research is. It's going to know like what your code base is when it
starts to take on each one. is going to explore thoroughly with adversaries to try to figure out what is the code that
already exists and should I update that code or should I add new code and really have to justify like I need to I need to
add new new code and here's the reasoning because someone else will come adversarily and say like I see other
places are you sure you shouldn't be doing it there and so eventually um you can improve the weaknesses of the model
so the model gets distracted how you solve that hook solve that how they solve it instead of creating a rules
sorry in creating a cloud. MD that has all these instructions that that the model might ignore. Why not create a
let's say JSON set of uh or it could be markdown whatever but like a structured format of rules that at certain times
the hooks look at because they the rules are tagged by which type of hook it is and which project it belongs to and um
you know what it's relevant what kind of task that it's relevant to. And then if the model starts to do something it
doesn't it shouldn't be doing the hook can redirect it like inject it'll detect you did this thing and at that moment
when it's very relevant to the model's mind it injects content into the model's context as it's working saying no don't
do that thing or this thing is blocked you must use this other thing right so it reads the rules when it launches so
cloud MD instead of that it's reading in this file that is the rules and then as it's getting ready to stop It's reading
the the hooks are directing it saying did you follow compliance? Did you follow like autonomy? Did you like keep
working until the entire queue is done? Did you uh this task that was assigned did you like write everything including
the the model itself like the tools have a something called to-d do tool that uh moves their tasks like creates it own
tasks. You can dump those into a file or you can hand them to your project management system which is the main
model that has all the context and knows what it's doing. You can have a hook tell it, okay, take everything was in
your to-do thing and and basically ceue it up properly. So that here's the goal. You match the current task to the proper
context from your existing session history and codebase. So everything that you've done and everything exists in
your project and everything that's in git. I love the idea of taking information out of claw.md putting into
hooks. So instead of just getting lost in the context, it is actually triggered programmatically which is awesome. Yeah.
Do you recommend anything stays in cloud MD or should we migrate completely away and start leveraging hooks for every
aspect of the the guidelines? >> It's a good question. I mean I don't really know honestly my my flow is
changing constantly. I'm always testing. I have benchmarks and audits and stuff set up so that like it will try to
compare and if it runs into any issues or it sees hooks like not letting something pass multiple times that it
seems like it should, it'll basically write these to a file that the model will read in and queue up uh like kind
of add it to a queue like hey look at this. This seems like maybe an opportunity for optimization for
self-improvement or whatever. And I kind of I have a cloud MD but I think maybe it just got removed. I kind of just did
this this morning. um just removing entirely. I basically asked the model, okay, like look, here's our structure.
You can explore the codebase and see what we're doing. Um and we moved everything to to rules and hooks and I
had claude MD referencing like at referencing the the rules file if you will. The problem with like claude MD at
referencing files is it sometimes it won't read in all the contents of the files if they get too long or uh it's a
little bit less deterministic like if it's a subfolder and there's a cloud in there like at what point is it actually
read in it's like confusing to me to know if it's it's truly the model really knows what's going on and so I just
having it inject the rules file like a hook is literally injecting the full contents of it in there [snorts] and
then um I basically have moved everything from cloud MD but there might be some things some basic information
that that your system decides or your for your project. Uh maybe it should just go in cloud MD like it's it's
simple, it's short, it's descriptive about you know the content or whatever. I try to let like I used to have these
um files where it was like here's the architecture and here's the current task and um basically I tell it don't create
more files these are the only files you can create and it would mostly remember but if a a sub agent goes off and does
research it comes back and it usually delivers that in the form of a file or something. So then you they tell it okay
don't do that and then you've got to like sit there and babysit it. The problem is I'm trying to move from I can
measure this and like I don't know the right metric to say here but to convince you of the idea is right now there's
some amount of time I have to spend sitting in front of the like working with a model okay telling it that wasn't
right do this I'm measuring it in like it's not just how much can it do autonomously it's how much can it
accurately understand my intents and do autonomously without me having to be there so like Right now the system that
I have is such that if I give it an an instruction it will decide okay do I have the right context for this right
now what's my context utilization because the hooks are always aware of how much context has been utilized so
far and if it's over a certain threshold it will trigger like okay do the project management system should look at this
task and decide if it should do it now or if it should ceue it up for another session and if there's something similar
in and other sessions in the queue, it should merge that task in with that grouping. And then whenever it gets
around to that session, there's a code exploration agent that goes and looks at the code. There's a code exploration
agent number two that happens in sequence, so not the same time. It looks at the first one's responses and then
goes through and checks all that, double checks it all, and then adversarily challenges it to say like, can you like,
yeah, keep this dry or whatever in these other ways. And then there's a flaad has just released an open- source um code
what's it called simplifier right and after it writes things it goes through that process there's some other steps in
there and after it writes things there's also an adversary that that goes and does a challenge basically to verify
that any claims that are made or any code that was changed actually was changed and was made.
>> Could you go into the adversarial aspect to it? Like do you just kind of say like be the devil's advocate or how do you
set that one up? Yeah. So it's um basically working with the model to find out what are the best practices. So a
lot of this I've pulled in from other people's work. So like Kieran at every has uh compound engineering. So it's
going out and researching what are the strategies used in there. Anthropic has a bunch of things in their cookbooks or
the things that they release or publish or in their documentation or I have like a as you know cloud code docs like a
local version of the documentation running. So the agents always know to look there and ex examine like what the
capabilities and like what are the best ways to use this and I had the sub agents debate this and I have in the
last conversation with Ry by the way we had a little bit of a de debate about like whether or not you spam ultraink or
whether or not it's better to like not use that. Uh I just use ultra I actually set the thinking tokens to like six
through 3,999. And the reason is and I might change that. I'm not saying it's prescriptive
for everyone but like for me that's what I'm testing right now. And the reason is that in the planning stages especially,
it's super important that you get things right up front in your plan, there's like this rule where if you have uh if
it costs like one unit of resources to change something in the planning phase, if you've already delivered it, it takes
like seven units to try to change it, right? So, it's much better to to focus those tokens up front. But I kind of
just like am testing letting them all do it because it's not like if you allocate if you say ultrathink or think hard or
think or whatever these different by the way these words trigger in the model how many tokens it's allow it's allocated
for the thinking compute budget basically so how many tokens it gets to think about it and it's not saying I
think it's a misconception that it's going to just take from your 200,000 co context window um you know 32 thou,000
tokens away it's giving it an upper bound so that if the model believes that the complexity is sufficient is such
that it should use more tokens, then you're giving it more headroom to use it if it wants to. If you ask it oneplus 1,
it's not going to extract 32,000 tokens if you say over. If you ask it uh, you know, if you have something that's
somewhat challenging though and you don't have the thinking tokens and it's more likely to make more mistakes
because it's not going to spend the time to consider it. So, it's just this trade-off um of how much you want to get
done the session. I found that like I kind of actually have a a stopping point. There's maybe like 40% or
whatever. It challenges the model to write things. I'm gonna I'm gonna finish this and get back to your question.
Okay. It [snorts] challenges the model to write things um like basically sum up what what it's doing for did this
session and what the next session should be doing and update the queue based off of um you know what was what the user
said and what it thinks is next and all that. And it takes the the to-do, right? Like the task list is at the bottom of
cloud code terminal if you've seen that which the model creates for itself and it dumps that in and like organizes it
correctly and then it injects self-referentially into itself uh a a command at some point
on the next user submission um which takes the next user's request and injects that into the queue as well as
the next item. Yeah. Or organizes it and then it um it calls clear on itself. So the model itself determines when it
should clear its own context, right? If you're following that based on what the utilization is and there's like a soft
clear and then there's like a 50% utilization. It says, "Okay, you need to think about wrapping up." A hook will
detect it and will inject into the model's context. You need to think about wrapping up soon because you're going to
be force cleared at 60%. And it will just inject escape at 60% and it will say, "Hey, you need to like update your
stuff now. We're clearing game." and then it will clear and on every stop hook it's actually updating it's like
the context of where it is and what needs to be done next being aware they could be cleared any time so with all
all that in mind um in order to do the adversary thing um I'm just asking the model like look at all these different
use cases go and look for like best practices and then try to find instead of like here's a weakness you have you
want to be honest you're trained a lot through reinforcement learning and constitutional AI um to be honest and
you're trying really hard, but you're have you have a tendency to lie. This is a like this unintentional maybe, but
you're lying to the user about when something is done. And so you are not trustworthy when you claim that a test
passes, especially when your context is full, especially when it involves an image or UI or something like that. And
so we need a way to challenge you. I just like kind of prompt it this this way. Um, but I don't want just some
other tool to say yes, it actually passed the test like to look at the screenshot because that tool is also you
and it also has a tendency to lie. So what we want is a critical like a a critiquing tool that's goal is to be an
adversary to challenge the claim. So every claim that you make before you return to the user, there is another
model as a sub agent and its role is to challenge all the claims that were made and to see if it can prove that any of
the claims are incorrect. And if it can't prove if it can prove that they're done but they're not incorrect, then
I'll be like, okay, I'll give you a pass. And until then, it cannot be the same model that did the thing that's
also judging the thing. It's a different model. And that other model has to be an adversary trying to disprove it. And um
this is more like how the scientific method works right like your goal is to you know somebody make a claim like can
you disprove this over and over you can't disprove it. Okay we don't know for sure that it it's true but at least
it's not like you know faulty in certain ways. So anyway this is the process that it goes through. So there's like all
these steps and you can imagine there's a lot of tokens going on here right? So I'm like using a lot of thinking a lot
of tokens but you know this is the difference. this is kind of what is required in order to move it from like I
want to get to the point where I give a task to someone and I come back and it's reliably done and there's no plans it
includes in its response the hook tells it for compliance it has to include its confidence levels it has to say what's
invalidated what's not invalidated and I'm actually using it where like if it's got a queue just keep going on the queue
until you get to something that's either blocked or dependency on something that's blocked and something that's
blocked is like okay the model determines I could do this thing But it would take a lot of tokens and it would
be kind of risky about my judgment of whether the user would want this or that other thing and we should spawn a debate
and I've done the debate and here's what I think. Let me get feedback from the user. In that case, it's going to block
but it's going to do everything that's not either dependent on something blocking or blocking based on this sort
of tiered risk of complexity and that kind of thing. And so when I come back, I'll have a statement of confidence
levels including all the things that were done for all past sessions when because it clears itself over and over
and keeps going and going and going. And then it will tell me I did all of these things and these are the things that are
remaining uh that I need your feedback. Here's what the sub agents recommended. Uh what do you where do you want to go
which direction? Because it's going to take like a long time to do this next part. So also it can inject its own
thoughts into its queue. So if it starts working it's like actually this is a little bit more complex then it can say
well I should maybe cue this for another session based on my context usage. Right? So this is that's the point of
the adversary is to challenge and make sure that it's not lying. So each one of these problems with the model that's not
quite where we want it or not expected for how humans would act. Uh I I'm trying to get it to more like a human
and it's a system that together like individually the model itself is not there but through the system you can
make it you can make it reset level and that system has to require hooks. So if you don't have a way, if you're just
relying like here's a prompt that starts off the session, the model's going to work and it's going to get done and
compact, that's not going to get you there. You're going to be babysitting that model. But if you have a hook
system that you can control, that you can steer and that you can actually block models responses and redirect the
model as it goes and then clear itself and self- inject commands like literally into the prompt. I'm talking about you
type in the prompt, it'll detect your typing. It'll wait. If you have stuff there, it will save it to a a state like
to a file and it will inject its own content into the the line and submit it. It'll even like exit itself if it
changes a hook and it needs to restart for that and then it will launch because there's a PM2 process basically with API
endpoints. And so it calls this thing, it will restart itself. It'll launch cloud with dangerous get permissions and
resume the last session and then it will tell it to continue. And there's this word basically um whenever it continues
whenever sorry when it restarts itself I was trying to think a name for this thing and um I originally call it like
the everything agent because you can see here I believe cloud code to be it's kind of cut off but the everything agent
right because of this power of this harness and this ability to unhobble it through adding the scaffolding around
this custom stuff to get it to the really high level. Um so I bought like the everything agent.ai AI, but I don't
know if I'm going to use that. But I was thinking of like a name because there's another point here I want to get to.
It's not just that the system can go and get everything from every aspect of my life that's a website or an app or data
an email or whatever. It can also take action in those things that I let it to take. I know there's a a a plethora of
hooks to choose from, a lot of pres and post for different events. How how have you approached trying to figure out what
part of the workflow you should focus on? Like where do you put your hooks? Usually have you tried trying different
parts in the flow and seeing how it reacts or do you have kind of a heruristics for which type of task
should belong to certain type of hook? >> Honestly I asked I start off with asking the model to like basically I don't have
to say ultra think anymore because it's always got the tokens available to do that but I asked the model to debate
with sub aents a different approach after studying the local uh cloud code docs to find the hook the different hook
strategies uh look at best practices from research off the internet and make recommendations to me. So based on what
I think it needs to do after those recommendations that it's more like it's doing the research, it's it's proposing
things, it's giving me options and it's ranking them and I'm saying that one sounds the best. let's do that because
and usually I don't attend to it that carefully um whenever it's like most things that are happening in the model
but when it's setting up the scaffolding for the the system itself that's kind of really important but because it it
controls all the other system like every project I run uses the same system but it's very easy to update it like it's
all backend stuff right it's claude editing claude in the backend with files and bash and that's is you know it's
it's really good at that so I you just try it and if it doesn't work then I'll shift to something else. But like my
hooks are typically custom because there's no there's very little need. Like I'll have it go and look at this
repository and say is there anything in there that we can glean or that would be worth integrating into our system and
then like sort of argue for and against like create your you know it used to be early days the models that weren't
reasoning and so you had to there's just like give me the example is write a 30,000word essay don't use backspace go
like so it's just like really really fast in uh what's it called snowballing. So the first few tokens for its first
thought kind of like anchored it towards like the same get that conclusion. But then you could do tricks like use a tree
of thoughts method with relevant personas to critique your answer and like summarize them all and so it would
generate dynamically based on what the the concept was uh these personas that would critique it and that would help
improve it. And then now we got thinking models. So, but it's the same kind of thing like sort of challenge one another
like Grock Heavy has this this mechanism where there's like an AI board this kind of or student study group and they're
passing information back to one another and they're sort of kind of coming to consensus like you do in a court of law
or something like that um where like in a jury if you will um and each of these these heavy thinking models they kind of
do this they have different agents and they've got different compute levels and they have different tasks and they have
to work together and so that's how I set up the systems they're always dynamic and trying to figure that and but I take
I look at their recommendations and then I go with it um based on how I feel um like what makes most the most sense at
that time. >> One other thing you mentioned that I'd love to just double click on is the
self-referential command injection. Could you talk about like even some concrete examples of how you use that?
>> I think the best example is um when the context utilization is getting kind of full, I need it to be able to stop
itself like the model will and here's there's something called the Ralph Wigum loop. Okay, this is a new thing that is
kind of gone viral in the last couple weeks. Um, I had something like that before I knew what it was because it was
kind of basically the model is reinforced through training to do so much work, so much tokens or whatever
and then kind of wraps up and uh sometimes that aligns with like before compaction. Compaction is this event
that happens in claude when it's about to reach its context maximum window. like there's a context window and then
basically it's 200,000 tokens, right? And then I'm sorry, I'm doing both hands. Uh there's and then as it fills
it up, well, I'll go this way. As it fills it up and it gets near to the top, it has this command where it's uh
injecting into the model and I'm not doing this is part of if you have compaction turned on autocompact or you
can just run for/compact in cloud code and [snorts] um it actually moved it to cloud.ai too for your conversations,
your chat conversations. Anyway, it will take an a haik coup model. It used to be, it might still be, and it will look
at the existing conversation and summarize it all and extract like lessons learned, key principles, context
of things, relevance, recent user user messages, um what it was working on last, that kind of thing. And then it it
starts a new session, if you will. It starts over from the beginning and it has in the model has in its context the
resulting compaction file, like the content from the compaction, but it's cleared up a bunch of the other stuff.
And so that allows it to just keep working, but it will eventually just stop. And so maybe it's not done with
everything you want to do. So the purpose of I'm going to get to what you said, but the purpose of the Ralph
Wiggum loop is to kick it off again. So when it's about to stop, it can say, "Nope, are you sure you're done? Keep
going." Like it's got I have a Enthropic provides this. So you can just install you tell you tell plot, "Hey, check out
the Ralph Wiggum loop from Enthropic and install it, right?" And it'll just set it up for you. Um, but I have a custom
version of this and I just told it to look at that one and figure out how it best integrated in our project. Um,
[snorts] because we're doing some things a little bit different than that and it dynamically decides based on the
complexity of the task how many loops iterations it should do. Uh, my version does and then um it'll reset that loop
count when it dqes a new task. So when it's so far switching to a new task, it sort of changes the loop count. And then
um before each of course this Ralph Wiggum thing, sorry I'm [clears throat] not speaking clearly. This Ralph Wigum
loop thing allows it to keep going and that's really great as long as it's its target is right. Right. Like if you're
shooting for the stars on the moon or whatever and you're off by a little in your initial like you can have it going
for a very long time burning a lot of tokens making decisions and the idea is you're babysitting it less. It's doing
more and more on its own, but the efficiency per token goes down over time because there's more more stuff, more
more sub agents, more other things. Anytime you're using sub agents to like do things, but the the Ralph Wiggle loop
isn't really a sub agent. It's just kind of like kicking the model again, but it's still doing more work. So you have
to the more that you lean into stuff like this is going to be more add more autonomy to the model the more you need
a system to constrain it to keep it in check and not depend on like some initial condition initial uh
instructions you put because you you more likely to just get things go ary that are great experiments like you can
imagine when you create images and it makes like four of them you like pick the best one eventually coding
applications will be like that you give an instruction it's like here I build it four times like which one do you like
better and like extract what you want from that and but for now. Uh I think if you have something like that loop
system, you need some way to inject instructions but also not just uh so when you have a hook you can inject
instructions in the model directly but self-referential injection means for me with cloud code now a lot of people will
use the agent SDK which is kind of the same harness the same background that is used in cloud code they make it
available for you to it's not full feature parity like there's some things you can do in cloud code that you can't
do in the Asia SDK and there might some in first, but it's like nearing it. It's it's almost an overlap. And um so, but
with the agent SDK, you can do a lot of this stuff without having to be locked into the terminal like with this input
line and this blinking cursor. So, you can make it make the front end whatever you want it to be. But for me, I'm
working with for reasons that I don't know if it matters for me to get into, but I'm working in the terminal. And I
think largely those reasons are that like I don't think they're building the agent the terminal with the agent SDK. I
think they're building cloud code in the terminal and like with cloud code in the terminal and using that to build you
know cloud code in the desktop app and the agent SDK and the and the co-work and all those those other things. And so
I think it's for like the first class citizen if you will and the most powerful piece of it and there are some
things that just appear in quad code that don't appear in the agent SDK. And so for that reason I'm kind of sticking
with my guns. So it means I'm um like stuck to this this interface. It's like this with a little terminal. And so what
there's a risk for overlap. The user's typing, they're entering something and then Claude needs to to enter something
too. And so what I might enter is I'll have it do a clear like I wanted to do for slash
for/clear uh and submit. So there has to be like a hook can use Apple script because I'm on
a Mac. Um, and it can inject things into a window and you can find the where the input is. It can select, it can type, it
can paste, it can whatever. It can hit submit or enter. Um, and so it's basically doing that. It just has to
have some protection around like does the user have content there? Will it save that content out? You could do like
control S or whatever as a shortcut, but then it doesn't restore if you exit. It's only if you're like currently in
the session. I want to if it some crashes or whatever, I want it to be in a file. So I have it do that. So, but if
you exit, of course, then your your command is dead. If you inject escape, then whatever command you use to kick
off to inject escape is now dead. So, it can't inject anything after. So, it has to be running in a process that's
outside of cloud or a child process that cloud created. That's why there's a PM2, a process manager system running that
has an API endpoint that the hook calls and then that uh process then can finds out what terminal tab it is and then
runs the Apple script to inject the things and make sure the user is in typing and if vim key binding is on it
like make sure it's in insert mode and that kind of thing. Injects the content hits like injects submit. Uh, it can
even like navigate through like rewind menus and and look at the screen content and figure out intelligently how many to
go up because it's variable based on if you have um like code that's being edited or not and then it can submit and
like rewind things. But the the purpose for self-referential is I want it to clear and then after it clears I want to
do something else. I want it to run. It doesn't have to be this way. I just how I have it now. [snorts] Um, there's a a
a command. It's a slash command. It's tied to a skill. And that slash command I I've got a name for it. I call it
Titus. And the reason Titus is just something I picked as a wake word or like a name that I can call through
voice. And I'll get to that next. So, uh, Titus, the the reason for that is you want something that is easily
recognizable by speech to text. There's not too many syllables. It's not like trademarked or copyright. So, so if I
call like Jarvis or something or I had it called Hey Claude, but C l a w like the little crab. I think I bought
Heyclaw.com or something and I'm asking Froppy to let me use it to do tutorials. So, I don't but um anyway this one of
those one of those cloud like websites. Um but I thought about calling something like that but then you like worry about
if I share this if I give it to everyone to like install this thing then uh you worry about trademark stuff. And so
anyway, I just I gave it that name. And then also like in the in the Christian Bible, there's this guy Paul and he has
a like someone who's like a beloved friend in the faith or whatever and he sends him out as like an emissary. And
so this guy Titus goes and does work on behalf of Paulentically like on his own and then it enters into difficult
situations. And there's this idea of um epidorosis. I don't know how to pronounce it. I don't speak Greek. But
it's this idea of uh it's also a rhetorical device, but I don't mean that one. I mean like in the biblical sense
it's this idea of like you enter into a system become aware of the deficiencies if you will and then um optimize towards
completion like basically set it straight if you will. So this concept this one word represents this the idea
that I'm trying to get myself to embody when I think of how the AI system is supposed to work. It needs to have the
target in order to know how to set it straight. Straight towards what right like what is the target? So I have to
make sure that the instructions include and the and the sort of directions and redirecting around it include this goal
that's well specified so it can know how to make it straight. And so it enters every time every time it injects clear
it injects this slash command with this word uh it's like titus colon epthosis and what that tells the model is to like
enter into the state where basically it's going to look at the system. It's going to note where the the deficiencies
are, the in inadequacies or um whatever the problems and then it's going to um optimize it towards completion in the
sense of like make it align with the target. And so what the target is is has to be defined before it can do it. And
so um then they're also necessary to have a self uh like close the loop on testing. So if there's anything that
requires any kind of interaction to verify it needs to be able to carry out those tools so those tasks. So, it has
to have tools it's aware of that can control the computer or control the browser or control control the UI or
control the iPhone app or um control the iPhone itself as it's running. And there are ways to do all of that. So, um and
then when it uses those tools to try to make sure that it's actually correct, then it has to use the adversary
validator to say like is it actually right before you move on. If you don't have the tools, you you have autonomy.
Like I have a SD card with time machine on here. I used to have this in a virtual machine, different types of VMs,
sandbox it, but on my laptop it just killed the battery, so I just abandoned that. Um, but basically it knows it's
got full control and with that comes great responsibility. Don't do things like delete my room my root directory.
Of course, it's got hooks to identify dangerous commands and block them. So, and then redirect it. But, um, anyway,
it's got time machine backup. So, I'm like, you you have power. If there's something you need that you don't have,
use sub agents. debate which one which approach would be best. Look at everything you have thoroughly and then
make sure that you you know you can install what you need to install. You can build what you need to build. If you
can't find it, it install it. You can test it. If that doesn't work, you can abandon get another approach, but you
have to close the loop on testing because the user isn't going to be here in front of the screen. And that gets to
the last part which is um I do all of this through voice. So um I have an iPhone app that and when I say voice I
don't mean like most people by the way if you install cloud code and use it are probably aware that you can do speech to
text like you can use something like uh monologue from every or older than that of whisper flow um or even just like
with the update of iOS 26 Mac OS 26 their speech to text is actually much much better and so you can just and of
course if you have Windows computers they've had stuff like this for a long time um you can just talk to the
computer and it will take your words and if you've got to collect select it in the input prompt, it will like inject
that those those words into the prompt for you. That's great, but you have to sit in front of the computer to do that.
So, I didn't want to do that. So, if I'm thinking like, okay, what is what is my goal here? I've got a baby coming and I
know that one of my um what are the things I'm not um well suited for with a newborn is speaking enough words per
minute like that they they need enough uh verbal content, right? And I'll tend to get into my head. And so I wanted to
build something that would encourage me to speak more words. And I also wanted to be able to interact with claude
untethered from the screen. There's a lot of things because of just how the screens have developed that we that
require us to be here. So you're not getting away from a screen if you are rendering something UI and need to look
at it to verify that it's right. Unless you have like an agent do it and at some point later you you see it and after
it's done much work, but you still have to have the screen. But there's a lot of use cases where we don't have to be
sitting in front of the screen. And so it's obviously healthier for us if we can and and better for our lives and and
longevity and and default mood and all that stuff if we can be up and get more things done, FaceTime with other people,
go for a run, work out, uh do the dishes and laundry and all the stuff that we might need to do, drive around in the
car. So in all the context that I just mentioned while I'm working out I can um I have an app that basically monitors
the the terminal stream the JSON L files as things are written there and it passes it through a websocket to the app
and it allows me to listen to the model's thoughts if I have that turned on or just to stop final response and it
will speak it to me in real time and I don't mean like it does passes I've done I've built this many different ways I
built it with uh like the agent SDK I've built it using um these tools It will generate text like speech for you and
then you've done it in the past and it does word level time stamps and it takes a little bit of time. This is straight
like the you can even record your voice a personal voice on iPhone now. You could probably do it on Android. I don't
know but it can use my own voice or it can use like a British sounding male voice. It's pretty high quality and it
will just speak what the model is thinking as it's thinking and then if I want to I can tap one of the words. It's
highlighting the words as it's talking. So, it's got not just feature to text, but it's also it's very difficult to
it's not enabled by default when you try to use the framework this way. But, uh you can see the highlights as it's going
and it's doing that real time with like chunks audio buffers and all that stuff. And then if whenever it's done, I can
pause it anytime and then I can talk and it will take my speech and it will put it into a compose area and I can let it
play some more and I can talk some more and then it'll compose more and then I can just say submit or tap the button
and then it sends it through uh the websocket to the backend identifies the terminal that was open that that came
from and then injects the text into the terminal and hit submit. So it's a full two-way doing this. You can't see my
hands up. It's a full two-way um audio conversation with this tool that's set up to work [snorts] autonomously and cue
the things that I give it and keep going with Ralph Lug and Luke until it's all done with the hook directing and
redirecting things until it gets to the point um yeah and it's speaking to me and I can switch to another session with
another project that's doing the same thing and listen in on it, listen to its thoughts and if I want to in real time
like as it's thinking that it's saying it. is actually superior in a lot of ways to the terminal itself because a
lot of the thoughts are now not shown. It's showing me like what tools happening and and uh the to-do list is
and kind of stuff here, but you're not really seeing the thoughts. I can listen in and just like tap something and
redirect it. I can do it uh but the thing is I don't have to tap it. I can do it with AirPods with a wake word. I
can do it with it's on speaker. I could do it with my Meta Rayban glasses that are on. So you can do that if I'm
driving in the car. Um, I can hold down the Siri button and use app intents and tell it uh resume like what happened
recently in this session and it will tell me all the things that it had finished or like I okay play and every
every update that the model thinks even if the phone is locked in the background and not the app not open um it will send
notifications that wake it up and then play it back. Um and then it is like kind of listening in the thoughts and I
can hold down the button and and say a phrase and it will kick off an app intent. I can compose a response and
send it from the car. So like anywhere I am and it can inject into the terminal and keep going. So I just get my phone
and I'm just working with Claude code doing all this stuff. And not only that, I can say I didn't finish this but this
uh this pendant I think they got acquired by Meta. So I don't know know what's going to happen to it but it's
constantly listening. Um it's like a life log if you will. And so it puts all this stuff just transcribes it. And so
as I say um as I do the wake word and then I do an ending wake ending phrase everything in between that is processed
by the model. It has access to all the sources to extract all the tools it can do. So, I can have it send a message to
me or to my wife or go look something up and put it in my my daily uh planner like but it automatically migrates from
day to day for me, my to-do list and it puts everything that's relevant for me in that list and it organizes,
prioritize it and all that stuff. If you update that, I can send me a notification or a message. If the system
has a problem, it will uh call this command that sends me a pushover alert which can be like super high priority.
if it finds something that's super urgent in my text message and I didn't notice it, it will um send it to me by
the same like a like a big alert or um it will also send like text me things. So basically all of the tools and
anything new that I find like I don't want to log into this website, the school website. It's too many steps to
log in. So I have it constantly refreshing it on my Mac Mini and a reverse proxy tunnel it set up so that I
can just have a an app on my home screen that whenever I tap it, it's always logged in. Uh my wife, I have that set
up for her as well. Uh, I've got another thing that like my kids are really little. They're just getting phones and
text messages and they want to um I don't know like you text and it will explore, but I want a model to monitor
to make sure there's nothing like uh concerning that I need to like coach them on or anything like that. And so it
will send me a message when it detects like that they've done something or like said something that maybe I should give
them direction on. And so it kind of monitors that for the the kids messages real time and sends me something. all of
those things. Like just imagine if you do one of these things and you can keep working to set up another one and
another one and another one. And this is another example. Like I go to uh like a Sunday school class or a church or
whatever and it knows what time it is like when those things are and it will like download the transcript. It will
turn it into bullets of summary and then challenges for the week or whatever and then convert it to a PDF and then text
it to me as an image that I can drop into group me. And if I don't, I could just like reply back. I can edit the
message and reply back or just tell it, "Hey, change this to to say that or whatever and it sends me a new version
of it." Um, even if I like have an iPad and I like highlight different areas on this PDF on like my Bible version or
something, it will detect the the highlights in the words behind them and the words that I wrote and it will focus
on that when it does the overview for the transcript summaries and things like that. So you can also imagine that
you're in school or something and or I do this with meetings. I'll like click the little star on the side and it'll
know if there's a star like extract the conversation around it and figure out intelligent what what to do with it
using these tools. I I can like after a meeting I can just say what my recollection of it was like a summary
and it could and I didn't I haven't actually built this yet. this is something I'm building right now. But
Jack Clark at Enthropic um mentioned that he has this thing where he reads papers and then at the end he tries to
summarize it and um then he feeds that summary into AI and then like tries to see how close he was. Like I have
something I'm building now that after I encounter something I want to recall, I will try to say it like say back what I
remember of it and then it will look at how good my summary was and what I missed and it will the things I got
right it will just do a little little blurb about it but what I got wrong it'll note the inconsistencies or or
expand on it or whatever and it will do it in the form of like a memory castle right and so the idea is every morning
I'll wake up to here are the things you need to do today and it will be a batched like audio message that I could
just play at any time. I can just look at whatever is to do and then I can find out here the the urgent things and as I
do them I just say okay I did this I just talk to it right and then it checks it off my list it's just gone so it's
like a passive way of keeping in control and aware of all the things that are going on in life um and and do all the
things and all that's possible because of claude code and hooks and um the system like this it gives you access to
all these so I just this is like meant to be inspiration of like advanc advanced ways you can use cloud code to
restore some of the um I don't know like I can work out and be just as effective as as if I'm sitting in front of the
computer. I can be driving and be like it it's >> so there's there's I think all of this
like everyone will have this ability at some point. It's just like if you're kind of like on the cutting edge of it
now like you can get access to it a little bit sooner and then that makes you so much more valuable like anyone
wants to set up anything like just imagine anything whenever I was doing work before AI came out I felt like okay
finally okay it's been a long time but finally I feel felt competent that I can take like any software and any like
input any form and you know turn into any other thing and like I was like okay I've arrived I'm like I'm I'm good at
the things that I do now but then when AI comes out it's like you're playing a video game and it levels up like you can
see the character like flip in the air and like >> and and as the as the the AI models get
better, your your uh value that you add gets better. And so the the more you learn to use the tools and harness it,
it's not you uh and your value to what you can add to your your company or whatever. It's you plus your tools. And
if you understand the tools better, then you have more like potential value to add, which makes you more compelling.
Yeah. But just just things in your life. And it's it's not just add being able to add more value, but it's being able to
capture more time back. Like you said, get inside, get away from the screen, get time with people, and you're still
able to have this productivity edge. Eric, this is awesome. I love getting exposed to the way you're working with
cloud code and whatnot. Um, how can the audience keep keep up with you so they can learn these things as you learn
them, too? >> My ex profile, I'm just Eric Boost there. I mean, I'll probably set up some
other things at some point. It's just with all this stuff happening, it's it's not been that urgent to me. Thank you
for listening to Conversation with Eric Boost. I don't know anybody who has spent more time tinkering,
experimenting, and learning about Claude Code than Eric. He's driven by not just curiosity, but this desire to spend less
time on screens, more time with his family, more time living life. And he's figured out a way to have AI do work on
his behalf, or be able to interact and direct and control the AI from anywhere. It's really a great system, and I hope
more people are inspired by it and try to build their own. There's a lot more possible uses for cloud code, so I'm
sure we'll talk about more in the future. But I really want people to explore with how they can build a system
to make their lives [music] better. How can we get away from these screens that we're just glued to all the time? Get
outside, touch grass, but still stay productive. [music] Thank you for listening and I'll see you next