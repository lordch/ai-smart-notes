# Chatting agents, context engineering and more with Dex Horthy (@dexhorthy)

**Source**: https://www.youtube.com/watch?v=BNhRnx_O95c
**Channel**: Chroma
**Date Retrieved**: 2025-12-09

---

## Transcript

Hey man, how's it going? >> What's up, dude? It's good to see you, man. >> It's good to see you. All right, so this is an experimental format, which is to say we just talk. Um, whenever we hang out, we seem to have great conversations about all things context engineering. And, uh, so here we are. We're in December of 25. Um, how are you thinking about context engineering? What are your latest thoughts?

So my favorite thing about context engineering actually I think I figured this out like a month or two ago but like I had posted that thing in like April 3rd or something right >> the 12 factor agents >> 12 factor agent thing right which is like had a article on like one of the one of the 12 factors was like about context engineering which apparently that was the one that blew up >> but like two weeks afterwards you just posted the words context engineering with no context and I'm like oh Jeff was thinking about the exact same thing at the exact same time as me and uh so that was exciting. I it's uh it's fun to have a a a secret co-creator of context engineering out there. >> I I don't remember if it was uh you know spontaneous evolution or uh if I just totally unintentionally loped and carpet copied you, but uh I could do worse than copy you. So yeah.

>> Yeah. >> One of the new words I'm seeing a lot is harness engineering. Have you seen this? >> I I tweeted about that unfortunately as well. >> I just tweeted about a guy. I was like, "Oh, yeah. This guy said it first." And then I was like, "Oh, no. That guy was actually reposting a post from another guy who I have literally talked to in the last two weeks." And I've read I've like seen the article. I didn't actually read it, but uh yeah, attribution is hard and I don't think anyone can really own a word for that long anyways. >> And who cares, right? It's kind of cringe to be like the person who coined X as like your name, your claim to fame anyways. So, I think we're aligned on that.

Um, what do you I mean new models are coming out every day in the past like three days, three weeks. So many new powerful models have come out. Like how have you updated your priors on like what it means to do context engineering with these like latest and greatest models?
>> Yeah. I mean I think I mean context engineering for me is like how do you get the most out of today's models? Yeah. If I was going to put it like at the top. A lot of people say, "Oh, it's all about putting the right information into the model." But it's like it's like it's it's getting the right information in, but also like keeping it as small as possible. And the keeping it as small as possible and as dense as possible is like the the thing that actually I think like not token dense, but like information per token density.

>> Uh so it's every time a new model comes out, we're obviously we're playing with it, we're testing it, we're working in different workflows. I think um a lot of what we are building on is built on kind of a paradigm that we're exploring a way past because I think there's a there's a new vision for it that is a little bit more flexible and makes it easier to take advantage of new models while they come out because today a lot of what we're doing and what we're building it's something that works really really well is like use a really smart model as your like top level steering orchestrator something like opus 45 or opus it was opus 41 forever. Opus 41 was the first thing that really like >> oh we can actually do really incredible things with this model.

Um and then you would delegate out like with your harness has sub aents which is one of the reasons we really like cloud code delegate out to a bunch of sub aents that use faster del models right we've seen this with cognition and sweetgraph we've seen this with warp just and like release their gp agent was it warp no morph sorry >> morph but it's called warp gp >> okay that's why okay [laughter] >> uh >> it's a lot of >> but one thing we've been exploring and it's actually um how the amp code team designed like AMP's been this architecture for a while where your like main orchestrator is actually a smart but not the smartest >> fast model. So they've been using sonnet >> as the default for a really long time um as kind of the core one and then they had this thing oh you can delegate out to a smart model.

They had like this oracle concept, right? And so they you put the reasoning and the really like beefy slow thinking intelligence. Hey, I have 50 files I need you to read and like try to help me figure out where this race condition is or something like that. >> Yes. uh and that becomes something you delegate and doing that really well is tricky because those big slow models are slow and if you're just like hey read these 50 files like >> I don't like sitting we've experimented with this using like sonnet as the driver and opus as the like thinker and the problem is is like opus is going to sit there and call tools and read every single file [laughter] and it's just slow because it's a big slow model they have the same thing with when when they had 03 as the Oracle um I'm sure it's GPT5 high now or whatever it is. I have I haven't checked in a while. >> Yeah.

>> But it's like Yeah. 03 is not great at tool calling and it's slow and so like if you actually wanted to read so there's like the context engineering nugget there is like okay well if you can have the the fast orchestrator model like figure out which files are relevant without having to like really understand every line of code >> you can put some deterministic layer in between that is just going to like stuff all those files into a big prompt and you kind of like step away or like >> you're you're deemphasizing the agentic loop loop and you're just like here's a crap ton of context tell me how it works or answer whatever the question is whether it's like explaining architecture things like that so >> the answer is like I think if we can the more people can move to that architecture and there's like a lot there and there's a lot to eval there's a lot to like figure out what the right just the right way of doing it beyond just like the vibes of us and our customers using it internally and trying it for us. Yep. >> Um,

>> this makes me think of another question which is like there's one school of thought which is like one model is all you need and maybe you're not even using sub agents, right? You're kind of just using like one model, one agent loop like you know multi-agent maybe like too brittle. This was the opinion at least you know a few months back for certain group of people. Um or like multimodel was also like either just like too hard to reason about or too brittle. Um and then obviously now you also I think increasingly seeing kind of this view or idea that like no actually like sub agents are really important for a lot of reasons and like breaking breaking out kind of agents into different roles and responsibilities which also begs the question like do you use like purpose-built models you know so take for like search for example uh you mentioned these like fast you know search agents these like you know models which are very good at using uh search tools and using them hopefully well um yeah what are what are your thoughts like you know is do we not you is the bitter lesson coming for all of us in the in the end of time like you know how durable is this is just a best practice for now and like we should just all embrace it because it is the best practice for now to use like multi-gage multimodel like what is how do you think about this in your head

>> well and yeah and you have orthogonal to the like I want to answer your question but not to get to you have orthogonal to like new models every week but then you also have like Ilia like scaling is not going to keep happening like we actually like we're we're getting near the plateau for the current set of technology and we need to go back to research for a while I don't I know if I buy that either. Uh >> and the real better lesson is that S curves are, you know, come for us all in the end. So >> Yeah. Yeah. >> Yeah. Well, but that's it's almost like the inverse, right? It's like, okay, if things are topping out, then now is the time to be investing in how do we get the most out of today's models? Because two years ago, you could be like, look at all this code we wrote so that GPT3.5 can actually like solve these problems. And it's like GPT4 comes out and you're like, oh yeah, we can throw all that out now.

It does feel now if you think about like the landscape of boxes that like an agent harness needs to do a good job. It's like okay maybe there's like a file system there's some level of like tools and tool use tool search um has the ability to inclusive inclusive of that like write and run code. Um it feels like the map of the boxes now is like it's going to be the same in 10 years. I can't imagine a world in which like those boxes change dramatically or go away, >> right? >> Like as long as we're dealing with quadratic like transformer attention, you're always going to benefit from doing the deterministic engineering that allows you to keep the context window as small as possible >> for a given task.

>> Yeah. >> Um there was more to your question. >> Let me ask a different way. Um, I've had this thought or thesis that like there's more than one class of inference workload. And what I mean by that is like people clearly understand like the beefy model, the beefy reasoner model. Yeah. >> Slow, hopefully methodical, very high reasoning power. Um, I think oftentimes if I'm just using, you know, TouchBT or Claude or Gemini or any of the models, I will often reach first for the high thinking model just because >> you want to see if I AI can do it. >> Yeah. It's kind of like see if I can do it. And it's almost like a script, you know? I don't not trying to optimize it. I'm running it one time. And so like, well, if I have to wait an extra 20% longer or even like, you know, 400% longer, I don't really care because it's kind of just like a one-off task.

um versus if I'm doing something in a loop and as a core part of my job like programming for example then like I obviously care much more about like it's like speed a thousand times in a day. Exactly. And so like I guess like you know are do you think of different like agents and sub agents as like demanding or deserving in some sense their own inference workload or to ask us another question another way like you know do you think that like there will be like dedicated models for search that will be uh that will you know be a will have staying power um do you think there be you do you think that context compaction is like an interesting candidate for like dedicated model inference as well like yeah how do you kind of think about the map of like agents and sub agents and like where it makes sense for like there to be like other models that are different than the high reasoning models.
>> I see. And this is in the context of the like what about the people who just say use one model for everything. It's good enough. And like yeah, you spend you waste more time minmaxing across all of them and developing intuition for all of them than if you like I tell this to a lot of people. was like, "Well, I use cloud code for this and I use codeex for this and sometimes I use cursor and then sometimes I'll shell out to deep research and it's like, >> yeah, >> you're only going to get to like 80% of the possible like the level of intuition that you could have with if you're constantly switching." Whereas like if you sit and talk to one model all day for like 2 months, >> you will develop a level of intuition that's actually that like that's where I think the people who are the best especially in the programming like using like what do we call it agentic engineering because I'm not saying vibe coding anymore. [laughter]

Uh but like yeah the agenda engineering world the people who are really good at this like have a really good intuition of the models and their context windows and like whe when to yell at them versus when to be supportive and all these like things that like are kind of feel a little bit like superstitious. >> Yeah. >> Uh but these people get results that I haven't seen anyone else be able to get. And so my advice is always like >> you will get better results if you pick one model, one tool and work with it a lot uh for a month or two >> and versus the like incremental gains you might get by like I mean unless you have like a huge eval set that's really really baked which most almost none of us do. >> Yeah. >> The incremental gains of like oh let me try the new DeepS okay let me try the new Opus and using a different model for three weeks every time.

>> Yeah. I I think there's more upside in just getting to know one model or one family of models really really well. >> That's interesting. Like I guess that implies that like the models are not at least at this point like highly swappable. Um you know you as a as a carpenter, if you will a master carpenter, right? Like anybody can pick up a saw and go saw some wood. Like you as a master carpenter really learn the characteristics of this saw for like this grain of wood. like your 10,000 hours and like you know maybe swapping saws out or swapping grains of wood or types of wood you do lose something

when CLI came out and uh especially the codeex model I think I think I saw Swick posting about this one too is like oh if you yell at codecs the way you're used to yelling at claude you completely de-une the model and you actually like screw up the performance a lot like all the all caps and like important and you must always is like >> is helpful and gets like good results from opus and things like this but um and opus actually getting much better at instruction following uh as well but yeah uh you go use the same prompts with a different model like we we've taken our prompts that are optimized for claude and opus and I've always said like oh our prompts are optimized for opus and like we basically only use sonnet for like searching and finding things versus like actually understanding how stuff works and like generating like summaries and documents and uh I think when I say that it's really like okay cool like I know that if I I have a sixstep workflow. I can rely on Opus to actually go through all those steps. And if I give that to Sonnet, it's going to get halfway through step three and it's going to forget that there was a step four, five, and six. I have to like remind it and you can change your workflow around that. But again, it's like cool. I know this works for this world and if I'm constantly trying to switch like I think Opus can do this, I think Sonic can do this. Now I need two sets of prompts and every time the models change, I need to update both of them. And it's like a whole thing.

H uh we were texting last week about the idea of like using AI more deeply and kind of just our like day-to-day work and productivity and specifically you're talking about like managing to-do lists. Uh like what is your current like personal to-do list setup and like do you use cloud code or like yeah if it's if it's just a piece of paper and and not AI related that's also okay but I was curious to sort of hear how you're thinking about how you're using AI and kind of your to-do list management. I
mean, everything's super chaotic right now, of course. Um, I think since bringing on a co-founder a couple months
ago, it has definitely changed because we need to be like when it's just you kind of steering the ship and every
like, you know, people on the team, you need to keep on the same page, but it's like it was enough for me just have a
pile of markdown files that I occasionally like sync to GitHub and think that was my system. And I used uh
I had I think I do you know the getting things done the like Robert Allen GTD? >> Yeah, GTD. So I was like, "Okay, cool."
Like deep research. Go make me a long summary of the GTD method and then drop that in a markdown file for Claude and
just like go implement this system and then it like kind of built the whole set of stuff. And I know lots of people have
done this. >> No, it was interesting. Yeah. >> Uh it actually ended up being really
heavyweight and like when we needed to collaborate more, we consolidated on like more of the like YC inspired like
okay, what's the goal for the month? What's the goal for the week? What's the goal for today? Check in at the
beginning of every day and at the end of every day like who did their thing? What's behind? what do we need to do?
And like constantly reorienting around like what's the most important thing >> and that just happens to work better in
a Google doc than in a markdown file. >> But there's no AI in that Google doc. It's just you guys as humans typing.
>> It's just us as humans typing. >> Do you think it should be like AIS like with you typing or would
>> I love that? Well, so this is also like a thing that we're um hoping to this is like not not not out yet and probably
not before the end of the year, but like collaborative markdown editing like >> isn't like there's just like I haven't
seen a good tool like VS Code Live Share is pretty good. uh but it's missing all the AI stuff and
like a collaborative workspace where two people can have multiple cursors on a document and also have multiple cursors
like in a prompt box and like back and forth with AI in a way that both people can see it and collaborate on this
stuff. I think that's >> a really interesting like y people talk about like oh chat is a is is a bad UX
for AI. we barely scratched the surface and also the web is like the preAI UX what's the new UX and I think it's like
the way that humans interact with AI and each other and can maintain visibility about what's going on is going to be a
really important and like very techn like the [clears throat] linear's entire company based on like hey we built Jira
but with a sync engine and obviously they're way more than that right they've done a lot in terms of design and things
like but at the core of it it's like >> it's a snappier better UI it's better for collaboration it feels real time
yeah and that's the That's the biggest unlock for me. >> Yeah. Yeah. Yeah. I think earlier this
year I like we'll just we'll be okay referencing your own tweets. Sure. >> Or zits in this room. It's a safe place
to do that. Um I tweeted something which is like you know most operating systems are built for single mode not for
multiplayer. And like for AI they need to be like multiplayer. Um and what I meant by that is like people quickly on
Twitter were like no you're wrong. There are demons. What are you talking about? And like okay fine but [laughter] like
you know you're not using my computer at the same time I'm using my computer. And this question of like file uh like diffs
and merging comes into play again like if we both have the same markdown file we both change the same line you know do
all markdown files need to be now like cdt native in a way that like the agents and the humans can all be editing at the
same time like >> yeah like you have thoughts you have to give away anything you have secret
thoughts about this okay okay figure that >> I mean they won't have to be but I think
you unlock a lot if you can solve that >> what okay that makes me think a lot about like AIUX it feels Like in some
ways AIUX is incredibly primitive still and it goes like kind of both in some ways. Well, there's two sides of this.
One is like AIUX is like actually really great and like chat is way better than people thought it was and you know it's
sort of wrong to like dunk on chat and like make fun of chat because actually like chat andor kind of like the you
know uh cloud code style chat is actually very powerful and you can do so much with it and so like maybe it's
wrong to dunk on that. In the same way it feels like we are in the caveman days of like again collaborating with agents
and other humans all in a shared workspace. And so like do you have thoughts around like I mean one
potential pattern which has emerged is this like inbox pattern where like the agent is like kind of teeing up
decisions for you a human to make and presumably it needs to give you all the context at the same time context
engineering for humans if you will so that you a human can make a good decision. But I guess like tell me more
about like AIUX like what are you using? What do you want to exist? Like what do you think is going to exist to run AIUX
that doesn't exist yet? Well, so the chat thing and the inbox thing is really interesting because I spent nine plus
months obsessing with this problem and like like I really when we were working on the kind of core human layer, which
we're kind of like sunsetting now, is like that was a really powerful like I thought that that was the most important
thing that was going to happen in AI. It was like people people dunk on chat and I actually like didn't like chat either
because it was like who wants to have seven browser tabs open for every single different agent that they have purchased
and they have access to, right? It's like I want to talk. The whole point of chat is like, oh, you interact with this
the same way you interact with other people. Like you text your friends, you type to the agent. Same experience. It
works. The issue was that like you couldn't actually, they weren't in Slack, they weren't in your email inbox.
Like the workflow that I came that like I thought was my favorite was like I had a bunch of emails and I've built
something where it's like you can just forward this email to an agent >> and it will like has a bunch of tools,
but the tools are wired with like an email-based human in the loop. So you get you delegate a bunch of stuff out.
Next time you come to your inbox, you have some inbound. It's like cool. Here's the like tool call I'm going to
make like your permission. It was a lot of like we were using linear as our CRM at the time. Okay.
>> Uh so I was like every time every inbound email I just forward and like add this to the CRM and it would either
make a new contact or add a comment to existing contact and all this. And so it like come back like here's the comment
I'm going to add and then I could reply it be like no do it this way or whatever it is. And and eventually when it was
good it would go actually update the CRM. And that's what I do. I don't use that agent much anymore because we've
moved our CRM into Markdown and Air Table and it's like managed by Claude and it's a whole it's it's not it's not
ready yet. It's not done yet. [laughter] >> I have so many questions about that. But maybe Yeah, keep going. Keep going.
>> Yeah, we can go. Uh but that was the uh that was my favorite AI UX ever is like talk to AI the way you talk to your
human co-workers. And I think the same thing is like some of the best collaboration experiences I've had are
like collaborative whiteboarding like everybody writing in a Google doc. Um physical whiteboarding is going to hard
be hard for AI but maybe eventually. Yeah. Like I worked I worked for like seven years at a company called
replicated.com. They did like like Kubernetes infrastructure for like deploying your SAS into like enterprise
environments and hired a bunch of like ex GitLab people which I don't know if you know
GitLab has like one of the most intense remote cultures like >> there's a whole like GitLab unleashed
YouTube channel where you can just like watch all their meetings and it's like what who are all these people? This is
absolutely insane. >> Yeah, like the the the being like fully open and transparent was like one
dimension of it but it was like there's things it was like >> okay every meeting needs to have an
agenda. If it doesn't have an agenda, it gets automatically deleted. Uh and like every meeting needs to be recorded and
if you are in a meeting and you're not participating, like you will be incur actively encouraged to leave.
[clears throat] >> Um because your goal is like if you just want to be in a meeting to feel
included, just watch the recording. And meetings are only for decision-making. They're not for getting on in sync. And
there's all this stuff like never answer someone's question. Someone asks a question, never answer it. You have to
respond with an answer like a link to the handbook page. And if the handbook page doesn't exist, you have to write it
and then send the link. And if the handbook page exists and then it but it's wrong. Like this forces people to
constantly go and review the documentation. Yeah. Is like if it's the only source of truth if like Slack is
not a knowledge. Anyway, there's all these like very strong rules and like everything's in a Google doc and
everyone's like collaboratively taking notes in every single meeting. I'm like this works really well. How is this
going to work with AI? Well, I think it's a lot better with AI, number one, because you don't have to have humans be
quite so much like robots. And that's kind of my critique of, >> you know, the proof is in the pudding,
right? Like obviously, yes, GitLab continues to be successful as a company as far as companies go, but like there's
a lot of stuff they've like missed and missed pretty significantly. And like you have to wonder like you know is the
over is the is is making product engineering a lot like a factory and it's like specification process
actually like removing some of the more like when are the water cooler conversations happening about like what
if we did this you know like where is a safe place to like bring up like a crazy idea and like let it be a crazy idea for
a while if every meeting has to have a agenda and a decision and you know like only people who are supposed to be there
are supposed to be there right? Like are you actually like clamping down on a lot of the potential like creativity and
upside um of like what could be >> Yeah. And this was the thing I Yeah. This is also part of why like we did
human layer like super all in on in person. It's just like >> I don't want it to be a chore to hang
out with my teammates and getting on a Zoom meeting is a chore. Yeah. >> I don't care if you're sitting around
having a beer. Like it's it's it's it's a thing I don't look forward to doing. I mean occasionally like during co like
Yes. cuz you're locked inside and you don't see anybody [laughter] ever. But it's like there's so much more that
happens in between the lines that you have to like counteract with all this overhead and rules versus like okay if
we can all just be in the same room then >> I don't know. Vib put this really really well which was like uh I think he put
this in the yeah in their like job posting was like you're going to be in person because work should be fun and in
person is just more fun. Like it's not fun to get on a Zoom with somebody most of the time.
>> Yep. I mean none of these things are like black and white true but it's just like
>> the the the spectrum is shifted significantly. >> Yeah. Are there other I mean going back
to AIUX kind of patterns right there sort of chat there's like this inbox pattern potentially. Are there other
patterns that you think are like useful or important or will be important? >> I mean I think tab complete is really
dope. I think tab complete is like the thing the thing the cursor figured out how to do really well is is super
impressive. >> Where do you want tab complete to work that it doesn't work right now?
uh for like non-ext things. >> Non-ext things. Say more. >> I mean, this was kind of like one of the
I think I was talking to Benny at Anthropic and I was explaining like what human layer was back in like last like a
year ago and it was like, "Okay, cool. Yeah, you have this agent out in the world." And then, you know, when things
are happening that need AI action, you get a Slack message or an email that's like, "Hey, we're going to do this
thing." And you're like, "Yep, looks good. Yep, looks good. And it was like it was like tab autocomplete for generic
tool calls based on you have something running in the background and it's like regularly like querying the state of the
world and deciding if there's some action that needs to be taken >> and then autocompleting that action
where it's like hey I'm going to send this email to this person or hey I'm going to update this record with this
data or whatever it is and you just be like yep yep yep no do it this way and then like kind of going through there.
It makes me think of this term which I think is kind of curse because there's already too many terms we should not
invent more terms but I will briefly say it is because >> oh let's do it. you've already heard the
term which is like organizations kind of having this like shared context layer >> um which is like exactly what it sounds
like you know the way same way a human has a mental map of like okay we do this in notion we do this in GitHub we do
this over here this is how all these tools like intersect and interact like presumably if you want an agent to be
another colleague sitting alongside you and doing useful labor and work it has to have a similar mental map of like how
to get work done and where to go look for certain information and how to connect it all together
>> is that a prompt and tools is that uh specialized like automatic query system. >> Yeah, it's probably it's probably prompt
and tools some agentic search thrown in for for fun. Um, so I'm not saying it's like a new set of of of components per
se, but I guess my question is like do you have talking to a few friends with this idea of almost like an AI
native organization and like it should run differently than like organizations have for the last like hundred years um
because the level of access to information is like so much faster and like I guess yeah what do you what do
you think about that? >> Yeah, I mean it it gives a little bit like 15 competing standards, right? or
14. What was it? Is like there's 14 and then someone's like there's too many we need to consolidate into one thing and
now you got another tool. [laughter] Uh if you win it it's if you win it it's great. Um yeah, I mean as far as AI
native or like uh trying to build the systems like kind of on the side in passive like hacking on
stuff that allow us to basically just use a pile of like we're doing markdown with front matter for a while because
front matter is nice because you can do a lot of like slicing and filtering deterministically without the model
having to actually go read the whole file. >> Interesting.
>> Um or use like the search tools. There's like a little tiny layer on top of the file system.
>> Yeah, that's cool. Um and then we have some stuff in air tableable as well which we're experimenting with and like
syncing between the two because what's the air tableable use case you mentioned this like CRM thing right like markdown
is the source of truth like what is air table like an ephemeral view for humans or
>> so we have uh I have a markdown system and then like we needed to like scale it to beyond me and like basically adding a
cloud command to sync it basically was like okay like commit pull the latest resolve the conflicts push it back up
and just like kind of have a post session hooked to just always like prompt it to do that basically.
>> Um that kind of worked but also >> air table a view to the data or was it also a
>> it's a view to the data but it's and then so yeah so we had the git sync and then we also have the air table sync and
it's like a birectional sync that is basically taking mostly stuff from the front matter like the actual like
structured data about a record and then taking the body of it and just putting it in like a notes field basically.
>> Um but it had like task management and stuff. It's very early. Like I don't know exactly how we're going to use it.
We're not using it all day. Um but it allows me to work uh by mostly just talking to Claude. And I can just be
like, >> "Hey, uh here's my here's my like I just had a call with this person. Here's
their email. Like go use the CRM writer agent, which is like a sub agent that is like prompted to like, hey, if you're
going to create a a person or a company and like link them together, whether you're creating a person or you're
creating a company, always go search the web." And it's like basically like a a poor man's uh like data enrichment
system. is like you can find most of this on the web and like Claude can just do it. I was like yeah I could go do
like clay and zoom info and like learn all this stuff but again I was just like >> if we can just do it with cloud and
markdown then that works great and like that makes everything a lot simpler and I'd rather have the like 80% or 90% and
just all one tool versus like specialized tools for every single part of the GTM stack.
>> It makes me So I've been hacking on a couple things on my own. One of them is like kind of to-do list management. Um,
and something about like it just being text as like kind of the actual storage layer markdown maybe markdown with
matter as you said like it's incredibly satisfying and I think that you do need like probably the CRDT story getting
like multiple people to like write the file at the same time. >> Um, but it's so flexible like there's no
database migrations like you're not like migrating your Postgress database to add a new field. You just like add a thing
to your front matter and it works. It's a little NoSQL, but like and you can also do you can do linting and stuff
like you can enforce schema in the front matter. You can just you know pre-commit hook
>> to reference another tweet I said like last week that no SQL is more AI friendly than SQL is. Um actually
strongly believe that. >> Yeah because AI data doesn't care about the schema. It's going to read the thing
and see all the stuff and >> schemes are for humans not for AI. >> Yeah.
>> Or or or or rigid schemas are at least. Yeah. >> So this is interesting. So I saw a tweet
recently that was like someone was talking about uh do you remember the tune thing?
>> Oh yeah. >> Yeah. I was like actually fundamentally I agree with the direction of this in
practice but the tweet about it was so over it was so clearly like part of the AI hype slop machine that I was just
like okay cool like saying a saying a correct or like somewhat correct thing in like a overhyped way like turns it
into slob. >> Uh but one of the things is like JSON was for humans and tune is for language
models. I'm like okay JSON first of all JSON is not for humans. JSON is for programs and I think front matter is for
like schemas are for programs. It makes your code safer or whatever it is. Yeah. >> I don't think human I mean
>> I don't know it all comes from spreadsheets right. >> Yeah. But okay going back to so you have
like the front matter which could be like your sorry the markdown which is like your source of truth of your your
CRM. >> Yeah. >> And this is like a schema the agent
itself can evolve right like the agent itself decide oh I need a new field great I add it. Maybe I'll back fill
maybe I won't backfill. It can just sort of decide how to evolve that schema. It's very flexible. Um, and then you
need the tools to be able to interact with that schema. Um, and the rules, right? And so there's sort of
conceptually some level of like rules engine that like the AI kind of can develop its own rules about how to
process, you know, certain CRM information. Then you also as a human might give the a agent uh sort of teach
it over time, right? Like you know if X and Y if you know A then B, you kind of give it more and more and more rules
that it should >> and it can refine. It's very easily to just be like, "Hey, we got too many
tags. Like, go refine the tags to less than 20 tag categories." Yes. And then go and then it's like, "Cool. Here's
what we're going to do. We're gonna do these the work back and forth." And it's like, "All right, cool. Let me go launch
10 sub agents to go update all those." >> But then you need the views as well. So right now it sounds like you're using
air table as this like complicated syncing view thing, but like why shouldn't there just like why doesn't
the agent itself just write >> some basic React app to like load that markdown into that local React app
>> and then flush it whenever you save it or you know even in real time be like flushing it basically like why do you
need a separate tool? I guess >> I just use an editor like I'll be I have uh I have a hook set up that basically
uh every week it goes and looks at everything on my calendar. I just like run it as part of my like Friday review
process. is like go look at all my meetings. >> Uh check who's not already in the CRM.
If it's external and they're not in the CRM and it looks like, you know, think about does it look like a sales meeting
or whatever it is. >> Pull them in. Um and we have the same thing like same thing for investors, for
customers, for like random users. We have like a folder of like just like they don't get an account, but they just
have like a CRM contact and it's just like >> cool, go create a record for them. And
then when I'm on a call with somebody, I open up my editor and I can pretty consistently just be like okay cool
here's who this person is. And it's so much faster than clicking around a web UI. Like it's just the the data is
already there. It's >> So you're using an IDE for this as your main interface.
>> Yes. >> But why does why does Air Table exist as a separate interface with the same data
>> for other people on the We have like a head of operations that does a lot of like automations and like non technical
people >> sends ex less technical people like he's semi. Yeah, exactly. He's he's dangerous
enough to run cloud code and ask questions and like he wrote a skill the other day like this is not like non
tech. It's just like people who prefer to work in something like Air Table, >> but presumably you could like build the
agent could build an Air Table clone. >> Yeah. >> And then you avoid the syncing problem
because like it's just some sort of like local sync story happening versus like another there's not another like durable
store of the same data, >> right? >> It's just like this like HTML page
almost that like knows how to load in a certain dur on your desktop. >> But you still have to get pull like we
store we store it all. It's like everyone's just pushing and pulling straight to master for that repo because
it's like plain text documents. So it's like even even without an air table like separate sync system there's still like
the repo or >> do you like get for this or do you feel like it's overly burdensome for this use
case? >> I basically just use it as like S3 or like a like generic document store right
like I mean being able to merge conflicts is great but again the CRDT thing is the actual answer. You don't
want to >> you would have no merge conflicts if you had CRDTs in theory or the CRTs would
handle the merge conflicts but git would not do the merge conflicts >> it and it would happen in an atomic
level and you would see it as it was happening like it would only happen as you were editing and you would see it as
it was happening >> I guess in you have like the logs some of like replay-ability for this repo but
like have you ever used that is actually like an important feature of that tool >> um no it's literally just like cool
before you start work poll like it's just we just built it in the prompts and like
>> it's annoying because it's a little slow right you're doing it on every call you're doing the same poll you're doing.
But like the thing the reason why we use cloud to do it instead of just writing a script is like because when there's
merge conflicts we have instructions in the prompts of like here's how to here's how to resolve merge conflicts and like
if it's really simple just do it for these sorts of files just keep both always because it's like a journal. It's
like a log of all the activity. It's like if it's going to get lots of conflicts but it's just like just make
sure that you keep the format correct. >> Yeah. >> Versus like some things is like okay
this person put this update and this person put this. It's almost always just like additive merge. There's very rarely
like >> for markdown files this have to like actually merge logic like you get with
code. >> Yes. Exactly. Exactly. >> Yeah. I think a lot of people are
reaching for git and I kind of like a suspicion that like that's not going to be a durable component. Clearly a shared
data store is incredibly important. >> Yeah. Maybe some version of some level of versioning is also very important but
like all the heaviness of git for something that's not code. >> Okay. So what do you need then? So you
need you need like local local local first speed, right? >> Yep.
>> You need like a UI that's accessible to less technical people at least for reading probably for writing.
>> Yeah. >> Yeah. And then you need like a very very like
I don't know high efficiency but well you know context respectful interface for an agent to use and ideally like if
you use the file system then cloud code can just go um yeah I mean you if you take uh
if you take uh your uh MBC architecture classic you Ruby on Rails, Django, right? Model view controllers, like what
is that? >> Uh the model is the schema of the data. It's the data itself.
>> But I don't want to have to think about the schema. >> I'm not saying you should think about
the schema. I'm just like teing up like another analogy I think like relates here. So like one is like there's the
data. The second one is there's the views. How do you view that data? And then the third one is the the logic,
right? Like the controllers are ultimately like your business logic. um or you know take any application what is
it and you sort of again it's like you know data compute and then some level of like pixels to kind of render back to
like the user you know the different things that they should be able to do. Um so I kind of wonder I'm imagining
this like >> what is the analog in the AI world? I mean, I think
>> could it be like markdown plus some sort of like rules, you know, AI rules engine. Where's the AI native version of
this? I guess >> I think the business logic goes in your prompts, right? We have a lot of slash
commands and sub agents that is just like like this thing that does the calendar. That's slash command. It just
runs like once a week in GitHub actions and it just like goes and pulls the things and then like pushes updates to
the markdown, commits and pushes it. Yep. >> Right.
>> Y >> um so markdown is is is part of it. Um, I think you need some kind of like
orchestration scheduling because you don't want to open this up and like tell it every time you want to do this.
That's kind of outside the AI. I think you need like tooling. You need ways to like the the the tricky part of this is
like, okay, how do I like figure out the Google Oath stuff, get the scopes right, actually off in, and it's like I'm not
going to build a web app that has full like OOTH like cycle because it's just me using it and I'm just using CLI
scripts. And so I was like, okay, like you need like a barebones like like O management layer and you need a way like
you need scripts and you need a way to write scripts and you need a way to >> like control. I mean, I was talking with
um Ian from Keycard about like MCP and like O and and like basically everyone just has like API keys littered anywhere
everywhere and that's terrifying because even the most fine grained off like something you get from Google or
something is really >> not I mean you have calendar readad and you have calendarmanage and those are
your options and like I want to be able to do like you can create events as long as they only have these people on the
invite and they're you're only allowed to delete events on my calendar if I'm the only like those kind of rules just
can't >> exist. very unsolved for like kind of this AI world.
>> So, and then I think you need a way to like write and execute code which is like is part of because then you can do
new things and you can generate new integrations and >> so it's like secrets management
>> code execution and like storing the executed code so you can like use it over and over again and then you need
like a data layer like markdown and then you obviously need some kind of agent harness.
>> Yep. >> What else? >> Uh views for humans.
>> Okay. like actual pixel pixel views. Um, >> which again feels like they could be this
>> that's been lowest priority for me because I just look at everything in the editor.
>> Well, true. You for your semi- techchnical users, you're talking about like doing things that feel complicated
to me which is like an air table like syncing engine for example when like you could just have like a view for those
users to the same data. >> Yeah, that's probably a better approach. Um,
by the way, the OTH thing can not be that hard. Like, >> over the weekend, I was building a
desktop app and I told OBS 4.5 to add OOTH for Google. >> And did it did it do like the local like
flow credential server. >> Mhm. >> Yeah.
>> Just one shot it. >> Yeah. It's been a year ago that did not work. You could not
>> It was like go easy. I was like I thought that I was like insane in my like to-do list. I was like this seems
kind of complicated and really hard. I don't know if this is gonna work. And I was like, "Yeah, let's just try."
>> Yeah. >> Um, and I was actually incredibly >> It walked you through going and like
creating the service account and downloading it. Like, had you ever done that before with like Google Ooth?
>> I had done it for Web Apps before, never for a desktop app, but it just did it just did it. One shoted it, which is
crazy. And did walk me through like, okay, go to the Google dashboard console, get these, you know, things.
So, >> so like that's another thing like models like that's I don't know if that's a
good benchmark. Uh, maybe that's one of my new benchmarks is like I was doing this uh a year ago with an agent. Do you
know codebuff? It was one of these coding CLI that came out way before cloud code. It was super
fast and it was only supported YOLO mode. There was no way to add permissions.
>> They had no complex inter like go just make it happen. It was very cool. [laughter]
>> Uh but I was back and forth with like I think it was on like a combination of like Gemini Pro 2.0 and like Claude 3.6
whatever. And >> it was like 10 or 15 rounds to get it working. And when it finally got the
oath and it could like list out my emails from Gmail, I was like literally typed in all cap. I don't ever done this
to model like holy, you did it. [laughter] >> Never have, but maybe I should, you
know. Yeah. >> Yeah. >> Um you you mentioned a lot about using
cloud code for a bunch of stuff. >> Yeah. >> Um are there other agent harnesses that
you're using? And if not, why not? Is like cloud code just the best or how do you think about this?
>> Every time a new one comes out, I'll try it for like an hour. Um, like when the new cursor agent view, I'm like I'm
interested more in like the UX and like the like how do you help humans keep all their work straight when their agents
can kind of go off and do things headless and you got to like maintain context and context switch a lot. So
like I played with the cursor agent view >> uh didn't get what I but again I was like now when I open any model I like
>> talk to it like I would talk to claude code and I was like cool I bet I could spend two weeks talking to this and not
10,000 hours but get my hundred hours and then be able to like >> actually know what it's good at and not
but I'd rather just keep focused on getting better and better at cloud code and like refining that. So we play with
codecs I've played with anti-gravity like we mess with all these things. Yeah, you clearly have a lot of thoughts
and feel for the limitations of either the models or the agent harness that they are given. Um, cloud code is not
open source so you can't change it. So even if you find a way that is weak, you have no ability presumably maybe you can
yell at [snorts] anthropic devril on Twitter and you know make some progress there. But
>> people do that. I try not to do that. [laughter] I I I I >> I have a lot of sympathy for Tariq and
the team after I [laughter] ended up I ended up going through like I I I opened an issue on the Antropic repo because I
was there was a cloud code like breaking change that came out with 2.0 >> and I like filed an issue and then I
like pinged the one guy I knew at Antropic at the time. I was like, "Hey, can you help me get this like uh like
escalated or whatever it is?" >> Yeah. >> And while I was waiting, I was like
reading through the other like there's like 6,000 open issues on the cloud code repo. Thousand opens issues.
>> Might be 4,000. I don't remember. It was like very it was in the thousands. >> It's intimidating.
>> And I read like five or six of them and I think five out of the six that I read were people just being like this thing
did a bad job on a coding test. I gave it this thing sucks. And I'm like man you guys I just think about like how
messy the signal is for a company that big with that much adoption and like I don't know how they make sense of it.
And I'd like >> hopefully AI but [laughter] >> yeah I would I would hope so.
>> But why not? I guess like going back to this like agent harness piece, you know, like
>> do you think there will be an open source equivalent to cloud code which is just as good or like open code exist?
>> I asked this again on Twitter maybe a week or two ago and resoundingly the comments were open code open code open
code open open code. >> Well because yeah because open code is basically built by like you can reverse
engineer the cloud code harness. Have you ever hooked up a proxy to cloud code and read all the traffic?
>> I know that you have. So yeah, >> you can do this. Uh it's actually like I did it yesterday cuz I'm building like
I'm rebuilding a lot of our like >> plan generation workflows to try to be we realize there's a lot of like
>> don't let me go on this tangent for too long but like we realize there's a lot of uh in using the like research plan
implement workflow which we shared and thousands of people have adopted on GitHub and like have grabbed the prompts
and put them in their own projects and are constantly being like these are the best this is state-of-the-art for like
using cloud code to like solve hard problems and complex code bases. I realized as we work actually in the
trenches with customers where we have like a couple champions and they're trying to roll it out to a team of 10 50
100 engineers um just like as an initial like test of like hey can we consolidate around one workflow for using AI in this
company and what we found is like when I use the prompts they're very different from how
most people use the prompts and most people haven't used them enough to know what a good session versus a not so good
session looks like >> um and part of it is like there's just like oh there's six instructions and if
you don't reinforce the instructions like okay now we're on phase three like please also do five four five and six
sometimes it'll just skip to the end or things like that >> and uh
>> I realized there's a lot of what I call like oral tradition this is the same thing of like people who used to be
really good prompters they're just like okay cool there's this thing where like okay you use this command and then you
tell it what you want and at the end you have to say like remember stay objective we don't want you to tell me how to
solve it just tell me how the codebase works today >> step by step Yeah,
>> exactly. Think step by step, all these kinds of things. And so what we're trying to do now is like how do we
>> how do we make the product um and the tooling less require that oral tradition? How do
we bake that into the opinions? And so it's funny is like I was a 12actor agents guy, right? I was like full fat
agents don't work. Just do context engineering. Treat LLM calls as just like an atomic step in your software
just like any other function. Yeah. And then two months later, cloud code like starts blowing up. And I'm like,
actually, full fat agents are good to go. I'm the cloud code guy now. Like, let's go. And now we're realizing like,
oh, the thing that we want to do is actually break up this workflow into a bunch of like smaller. There's like a
chat loop. And then you progress the conversation to another part of the chat loop. And so, it's like, oh, we're back
to >> context engineering and micro agents. If you know what the steps are, don't rely
on the prompt for control flow. If you know what the workflow is, split the prompt up into smaller workflow steps.
You can still iterate with the human in those steps and then explicitly proceed to the next one either by a model doing
a specific structured output or by the user opting in like yes, I'm done with the questions phase. Now I want to go to
the plan outline phase. >> Any working on this and it's really fun to like build an AI product from scratch
with like really good evals from day one because we know exactly what we're doing. And so like
>> uh but one of the things I built was like to be able to really diagnose this and understand things is from day one
the whole system has uh a logging proxy everything gets proxied through and we log every single request response pair.
So whenever anything happens we can say like hey go look in the logs here's the exact response from anthropic like
reverse engineer cloud code from the outside because it is closed source. >> Yep.
>> Um >> so why not switch to open code? >> Uh no comment. Okay,
>> may be coming. >> Okay, cool. Uh, but yeah, open code's great because it was basically you
proxied it and it's just like a token for token replica of cloud code because you can pass the same tools, you can
pass the same tool definitions, you can use the same models, right? >> You can make the tools behave in the
exact same way, right? >> And that's why open code is tied with cloud code on most of the benchmarks
because it's the same thing. It's just open source. >> Right. Right.
Um, speaking about evals, >> yeah,
>> popular topic in the press. Um, >> big I got cooked by big eval, man. >> Let's get into that. [laughter] Uh,
yeah, big eval. It exists. Uh, I wrote my notes here. There's a million AI observability companies. Um, many of
them very wellunded. Um, and then there's also everybody saying actually LM's judge doesn't really work very
well. Like actually, actually, actually actually, how do you do emails? Oh man, LLM is
judge. I was working with a customer a long time ago um and they were like, "Hey, we're gonna do I was like, I don't
think LM is judge works very well." Like I don't think models are good at evaluating things. Like when we do when
we work, we try to keep the model objective as long as possible. And Kyle actually just put a post on like a good
clot MD. Uh and part of it is like never send an AI to do a llinter's job. Like anything that can be done
deterministically, >> like I don't trust a model to read code and tell me if it's good or not
>> because these models are like optimize, optimize, optimize to tell us what we want to hear. And you could say, hey,
like review this code and tell me if it's good or not. It's like, yep, it's great. Like, hey, review this code and
tell me if it's bad or not. It's like, yeah, it's trash. And it's like, it all depends on how you phrase the question.
>> Yeah, I've heard I've heard the I asked the question again online like, you know, how do you get like valuable
critique from one of the models? And it was like you have to tell it. >> My friend sent me this uh and I want to
give them some valuable advice, you know, like what should I tell them basically otherwise the model will like
think that you know >> it doesn't want to hurt your feelings. >> Exactly. Exactly. [laughter] Yeah. Yeah.
Yeah. >> So yeah, the element judge thing is interesting. I mean there's a lot to be
said for like evaluating the like objective characteristics of it. is like you know we do in AI tinkerers we have
an algorithm on the back end that is like hey cool like we want to make sure that this event is mostly like by
builders for builders and so we don't ask like hey AI rank this person on a scale of 0 to thousand on how technical
they are it's like no extract like 50 data points and then we have like an algorithm that turns that into a 1 to a
thousand score it's like have they had a software engineering job in the last two years do they have they pushed anything
to GitHub does their GitHub stuff have AI stuff in it you know it's all these like you know there's 50 questions I
actually don't know how ex it works Exactly. But I know I've reverse engineered it by uh the number of bugs
I've reported in it, but it's it's getting [laughter] really good now. Um so as far as observability goes, I
don't I don't know. Uh >> you just said we have very good evals. What are your evals?
>> Uh they are snapshot based. >> What does that mean? >> Uh so um we did an episode uh about
evals with um with Viob and there's a bunch of different categories and like we don't have most of these.
>> We'll link to it in the show notes. I guess the show. >> It's really fun. It's from like it's
from like 4 months ago and like I haven't seen anything like Vib led the episode so I'm happy to talk about how
great it is. I haven't seen anything of like higher signal and like value density as far as like how to do good
evals since then. >> Okay. >> Um and to be fair like I don't get that
excited about evals. Um so if I'm sure if I looked harder I would find some really good stuff.
>> Yeah. >> Uh but essentially you know we have this prompt workflow and it's split into
stages. And so we have a test that like runs it end to end for a question. It takes kind of like a long like cloud
code running sub sub aents searching files doing all this stuff. >> And then we output the snapshot
basically here's what the final output was. And then we can also break down and do eval stage kind of like unit test
versus integration test kind of thing. >> Um but even the unit test is around kind of a large part of the workflow.
>> Yeah. Uh and then we just store the output and then when you run it, you create a set of new snapshots and then
you can diff the snapshots uh in the CLI. We'll probably build a web. It's very easy to vibe code a web UI for
these things. >> Totally. >> And then um
>> and then you can accept the new snapshots. It's like okay that change is better and I like that like oh I made a
change and it has changed significantly >> then but it's basically the the ability to like because eval for me are
>> I think of them the way like software engineers like think about unit tests or integration tests or end to end tests.
It's like a way to prevent regressions. >> Yeah. >> Right. Yeah.
>> And so you can have the very low-level unit testy eval which is like okay this comes out and I make a bunch of
deterministic assertions about the output. really nice for like structured output problems and like like like
parsing unstructured data into like structured objects. You can make a lot of assumptions. You can make a lot of
assertions there. >> Yep. >> Uh but we're not we're not there yet. So
it's like I don't know. The advice that I like the most is like like anything like the first layer is vibes. Vibes is
very high leverage especially if you don't know what you're building yet and you don't know what you want it to look
like. >> Um I think there was a guy who talked to AI engineer worlds fair um Ben Stein. He
talked about like how does product management change in a world where like the capabilities of what you're building
are emergent. Like you don't actually even know what it's capable of until you build it and like try it on a bunch of
stuff. >> Yeah. >> And so his flow is like the BDD thing
never really worked anyways. They're like okay like let me define the behaviors that I want and then work
backwards from that and then that's what we evaluate, right? and like building the evals first for an AI tool
>> feels his take is like that's you're going to constrain what you're actually building
versus like build the thing have a product manager play with it for a couple days and then have them like
point out okay these are the behaviors we really like >> here's the bugs but like then you back
into okay here's what we're going to email against going forward. Yep. Yep. Um, continuing that thought, but also
changing a little bit. Um, >> the the topic of like continual learning has been in the news extensively also
recently through like 18 of Dwarf Cesh's podcast now basically, but also most notably um the most recent one with
Ilia. Um, >> summarize it for me because I've I I've been like kind of following, but like
what's your understanding? You've clearly consumed more of this than I have. It just seems like there's an
increasing awareness that like what we really want is the ability for these AI systems to be able to get better through
experience. >> Okay. >> So the AI system goes out, we tell it to
do a job, it does the job, it observes what it does well, what it does not do well. It also gets feedback from humans
about what it's doing well, what it's not doing well, and then it's able to sort of update its intuition about how
to do that thing and then get better over time. This is how we this is how humans operate, right? like you could
not write a manual that was detailed enough to onboard an engineer onto your team and oneshot it. Um, in practice,
you're going to be like sitting next to that person and like giving them micro feedback for months to like get them to
be like 100%, you know, autonomous basically, >> but you're also not writing down all
that feedback. You expect them to write down the feedback either internally or on paper.
>> No. Exactly. Exactly. And so, you know, yeah, the tacet knowledge transfer is is is a big problem broadly, right? Even in
human systems. Um, >> but I guess that we it feels that that is like what we all want these AI
systems able to do because like again you use the thing and you notice where it makes mistakes and then you need to
now try to up either work around those mistakes and or like try to teach it itself to avoid those mistakes and then
ideally again there's like some aspect where like it can just do that in the weights because that's presumably more
expressive than like adjusting the prompt or adjusting like the rag system it has access to or whatever
>> or like adding adding directives to the end of your cloud MD. right? Like CL has this memory. You do like a hash thing
and then it's like cool, I'm going to memorize that instruction, >> right?
>> Um, but you want it to update its own stuff, right? So there's like some level of like maybe like offline like
compaction where like the model so the the current version I think I've seen people now increasingly trying to do I'm
not sure how successful it is is like you know every night the model itself goes back through everything it did that
day and then it like reflects on like oh like across these like hundred traces like what could I do better and then
like tries to like bake that into its knowledge for the next day or some level of back testing to see if that works for
the previous week or you can kind of imagine the sort of offline compaction system that obviously can also a
training loop as well. So there could be like continuous RL or whatever on top of the model. But like I guess thoughts
about continual learning broadly. >> I mean it sounds like the the naive solution is like build a good memory and
not naive in the sense like it's building a good memory system is really freaking hard.
>> Yeah. Why is it so hard? >> Um I think it's hard to do. I think it's
almost impossible to do generically right now. I think like you can build really low-level building blocks. Um I
think building a like thick horizontal memory layer is this like models are changing too much, the use cases are
changing too much, the engineering techniques are changing too much. Um I know people who are building for a very
specific use case like my buddy Brian is at an applied AI lab. They built like a tutor and so this AI has uh they
implemented from scratch because this is the only thing that gave them enough control was like a they call it like
decaying resolution memory. And so every time the agent turns on it's like cool here's what's happened today. Yeah,
>> here's like daily summaries for the last 14 days. Here's weekly summaries for the like three weeks before that. And then
here's monthly summaries for the last two. Like it's not like conceptually hard.
>> It's like an educational use case like teaching somebody how to Yeah. >> It's does like tutoring for like grade
school and high school students basically. And so it like receives emails from parents. It receive emails
from students. It receives like a daily wake up to just see like, hey, is there anything to do today? Here's your rules
and here's your memory and stuff like this. >> Yep. and uh like but that's a very
specific implication for a very specific use case and I think if they had tried to generalize it they would not have
solved their own problem and they would not have also not have solved anybody else's problem
>> I guess not that I mean the general case is obviously very interesting because you can then in theoretically point this
agent at anything and it sort of just will get better uh naturally so that's interesting from that perspective but
like I think for now >> for people who are builders the ability to build agent memory successfully for
my use case Yeah. >> Sort of a proxy to continual learning. It sounds like you're seeing some people
like be successful at that, but it sounds like it's like not easy still. >> And it's not it's less about behavior,
right? It's more about like factual recall of like what are the things I need to know to do my job? And like the
actual continual learning is like because they need really good performance. They're they're not willing
to let the agent update its own memories. They're not willing to let the agent like update its own instructions.
Like >> the memory layer is the single like system of continuity through the whole
thing. I think I haven't I haven't talked I talked to him for about it for an hour, you know.
>> Yeah. Yeah. Yeah. >> But I >> the factual stuff feels doable today,
right? Like remember this user likes potatoes like that. They don't like >> lettuce. Like I the factual stuff feels
like fairly doable. Like the thematic stuff like it feels like much harder. Um >> like the the instructions and the rules
like the the how to be not the like what is true, >> right?
>> Yes. Yes. Yes. Yes. Have you seen anybody attempt that? [snorts]
>> I mean, I see a lot of people like try to attempt it in their cloud MD files and it doesn't it doesn't go very well.
>> But why is that? Is it like the model, the harness or all the >> I mean, there's some there's some
finding and like the I think the stud is like six months old at this point. So, there's no Gemini 3 or anything in
there, but it's like >> models can follow Frontier models can follow about 100 to 200 instructions or
150 to 200 instructions. And if you give more than that, you basically like really start to lose out on you spread
the attention across all the instructions. The model's got to try to decide which ones are relevant and
sometimes it won't. >> Um, >> this is like context rot for tools
basically. >> Four instructions. Yeah, exactly. It's like you tell it too many ways to do
things, it just like won't work. And so people just like spam with like always do this, never do this, always do this.
And like you put the all caps thing, that's going to put more attention there. That's going to take away
attention from everything else. And so you have this like almost like instruction severity inflation where
everybody who wants to add a new instruction wants it to be followed. So they put theirs in all caps and then the
the other ones get followed last and then everyone is coming in and suddenly your entire like memory like instruction
system your whole system prompt is just like everything's in all caps and you're actually like d-tuning it from
everything else in the conversation. >> Why is like I guess aentic search not a solution to that problem? Like anthropic
just launched their like tool search thing for example like seems like rules search in this context would also be
like potentially very effective. >> Oh I haven't yeah I haven't I haven't seen anybody implement that.
>> Oh okay >> of like hey I'm doing this like how should I perform it and then you like
rag against it or something. >> All right. Well I know we're hacking now.
>> Yeah. Rules bench. >> All right. Great. >> I'm sure there's a lot of instruction
following benchmarks. I don't know if anyone's evaluated anything like that. If you're on the YouTube, ping us on
Twitter and tell us cuz uh I would be interested in hearing more about that. >> Yep.
>> All right, we just hit an hour. >> Damn. Really? >> That was an hour.
>> Okay, >> we could talk all day. It >> was fun.
>> Uh but why don't we call it there and save the good stuff next time? >> Sounds great. Can't wait.
>> Good stuff, dude. Peace. Cheers. See you.