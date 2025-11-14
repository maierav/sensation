# SENSATION AND PERCEPTION

This web site is meant to provide a gentle introduction to the science of sensation and perception, with a few select scholarly references provided for deeper self-study. 

% Perception
:::{figure} images/Mach.png
:label: fig:perception
:alt: Perception
:width: 60%

Sketch of Ernst Mach of visual perception with the right eye closed.
:::

We will start with an interesting observation about perception that seems to counter our intuitions and ponder its basic philosophical implications. We then will try to work our way from the philosophical insights (i.e., the deepest foundations we can find) to modern science. This exercise will involve taking on a bit of formal logic and mathematics before investigating if these tools of science can be applied to perception. We then will review the psychology and neuroscience of sensation and perception, which provides the bulk of our modern knowledge about perception. Much of this work is focused on vision (seeing), but we will also review our other modalities (senses). Lastly, we will return to mathematics and explore whether everything we have learned can be synthesized into a coherent view that merges the philosophy, psychology, and neuroscience of perception. Interested? Then, let us get started!

:::{tip}
:class: dropdown
:open: true
Stop your reading each time you hit a box like this one. Sometimes these will be questions. Think about them for a moment and ask yourself how you would answer them before you continue reading. Sometimes these boxes will provide definitions. Ask yourself if you agree with them, and if not, how you would define the concept instead. If the box provides online links, check them out to see if they provide additional information that is new to you.
:::


## MOTIVATION

Imagine what it would look like inside a giant room that is uniformly filled with very thick (dense) fog and uniformly illuminated with ambient red light. All we can see all around us is red fog (Figure 1).

% AI render of dense red fog
:::{figure} images/red_haze.png
:label: fig:red_haze
:alt: Thick, uniform red haze
:width: 100%

Imagine you are deep inside thick, red fog.
:::

In this (hypothetical) situation, it seems like we can just perceive "redness" all around us without also seeing a distinct shape. Let us consider that for a moment. What do we actually perceive here? What is that - "red"? Can we be more precise in describing what that is the "redness of red" that makes up virtually all of our visual perception in this scenario? 

:::{admonition} ❓ Question
:class: dropdown
:open: true
:icon: false
How would you explain what "red" looks like to someone who was born blind?
:::

At first, we may think that there are indeed ways to describe red. After all, we use "red" in many other contexts other than when we describe the color (e.g., in calling anger "seeing red").

:::{hint}
:class: dropdown
Is it helpful to describe red using associated concepts, such as "warm", "heat", or "love"? 

Are these associations helpful for someone to understand what redness looks like if that person has never seen fire, or a heart symbol (such as this: ❤️)?
:::

Deeper reflection makes clear that there seems to be an interesting problem about the simple perception of red. If someone, for some reason, would see what we see as "green" whenever we see "red", it seems virtually impossible to find a way to find that out. Whenever we try to see if our perception, of say, a ripe tomato is the _same_ red, that person (who actually sees it as what we see as green) would agree with us that this is "red". After all, anything else that we call "red", they have called "red" their whole lives as well. How could they know that we see that color differently? 

This thought experiment has fascinated people since centuries, and it has been termed the **inverted spectrum problem** [^1]. 

[^1]: If you are interested to learn more, check out this free, [scholarly overview](https://plato.stanford.edu/entries/qualia-inverted/).

% Inverted Spectrum Problem
:::{figure} images/inverted_spectrum.png
:label: fig: inverted_spectrum
:alt: Inverted Spectrum Problem
:width: 80%

The Inverted Spectrum Problem. If there were people among us who see red as green and green as red, it seems like they and us would never be able to find out.
:::

## FOUNDATIONS

Now that we had to acknowledge that there is something about perception that seems puzzling, we may ask ourselves how we got there. 

You may be burning to start learning about the science of perception. After all, the brain is very interesting, and there is indeed a lot of fascinating material to learn there. However, as you will see, the puzzle of perception **will remain**. 

We thus might do best to first spend a bit more time ensuring that the house of knowledge that we are about to build has solid foundations. Otherwise, you might feel later on, that we already went wrong somewhere early on. On the flip side, if we carefully establish our starting point first and then carefully build up from there, we may find that the puzzle of perception cannot simply be explained away because we launched into neuroscience too hastily.

### Epistemology

Epistemology is the philsosophical discipline that is interested in finding out if and how we can know anything. That seems like a good start when embarking on a journey of gaining greater knowledge. We first should ask ourselves if we can know anything in the first place, and then clarify how we can know anything, and where the limits of knowability might lie.

To make that a bit more tangible, let us do a quick thought experiment:

:::{admonition} ❓ Question
:class: dropdown
:open: true
:icon: false
Can you be certain that you are awake right now and not dreaming?

Can you be certain that you are not living inside a VR simulation (like in the matrix movies)?

Can you be certain that you were not just coming into existence with the rest of the world a minute ago, with everyone who also came into existence at this point and yourself coming into existence with the memories of "a time before"?

How can all these be ruled out?
:::

#### Agrippa's Trilemma

Kids sometimes go through a phase where they keep asking "But why?". Something interesting happens in these situations: They seem justified in keep asking "But why?". 

Imagine a parent tells a kid that is time to go to sleep. The kid asks "But why?" 

The parent might reply "Because it is late and you are tired."

"But why?"

"Because our bodies have a need to sleep - that is why you feel tired."

"But why?"

At this point, a parent might have to admit that we do not actually know why animals periodically go into rest periods. Or perhaps the parent might go on and explain that there are some ideas why we have a need to sleep. But the kid can go on asking "But why?". Usually, the parent will at some point just end this line of inquiry by saying something like "Because it is so." However, both the parent and the kid will understand that this is not satisfying.

Thinkers have long realized that this is interesting. These thinkers have come to the conclusion that there seemingly are only three ways that a consistent chain of asking "But why?" leads to one of three outcomes:

(1) We end the inquiry by stating something that can no further be questioned (such as: "all animals need sleep"). We might call these unquestionable assumptioms "dogma", or "axioms". Either way, these are foundational - yet unfounded (unsupported) - beliefs for which can no further ago. Accordingly this starting point to knowledge from which we can build up answers to "why?" questions is called **Foundationalism**.

(2) We end up going around in circles. That is, we embrace circular logic. We might end up saying that at the end of "But why?" questions we find two statements that support each other (such as: "all animals sleep" and that is because "without sleep animals cannot stay awake"). Supporting this outcome is called **Coherentism**. 

(3) We could also opt for just keeping the "But why?" inquiry going on forever (such as going on about why we think that animals sleep and why we think that this tells us what is the case and why we believe that things are the case and so on). This solution to the problem of seemingly ending "But why?" questions is to counter them with never ending answers. This stance is called **Infinite Regress**. This may seem satisfying at first sight, but there is a certain absurdity that comes with the assumption that there is no starting point to knowledge. the psychologist William James explains this with a joke: 

“The old lady said that the world rests on a big turtle.
The scientist asked what the turtle rested on.
‘Another turtle.’
‘And what does that turtle rest on?’
‘You can’t fool me, young man—it’s turtles all the way down!’ ”

It is important to note that all three of these potential outcomes are on equal footing: There is no way to logically argue why one of them is preferable over the others. This realization is known as **Agrippa's Trilemma** (also called the Munchhausen Trilemma). It is a dilemma, or more accurately - a trilemma, because none of these three options seem satisfying. Neither for kids, mnor for adults.

As we will see, mathematics seems to choose Foundationalism over the other two possibilities. And as we will see, mathematics is _indispensable_ for science. We hence will aim to start with a foundationalist stance. That is, we will start with a few statements that are hopefully agreeable as non-questionable starting points. We will earmark them as "preliminary", however. That is, once we arrived at deeper insight we might want to come back to these foundational beliefs and examine whether we still agree with the assumptions that we started from.

#### Preliminary Definitions

_Sensation_ is the process our bodies undergo when acquiring information from our environment, such as when a touch sensor in our skin gets depressed. We are not aware of these processes, and many of them occur even when we are in dreamless sleep, coma, or general anesthesia. Sensation is an unconscious process.

:::{note}✍️ Note
:icon: false
Our _senses_ detect and quantify _changes_ in our *physical* environment. 
:::

_Perception_ is what we *experience*. The most common notion of perception is the experience following the process of sensation. That is perception is conscious (arguably the biggest part, or even all of our conscious experience). Let's call that **perception in a narrow sense**. 

Note, however, that a very similar state of perception can also happens without sensation, fully discoupled from the real world, such as when we hallucinate or dream. You can see a face either being looking at a physical stimulus, such as another person or photograph. But you can also see a face in dream sleep, with your eyes closed in darkness. 

In this light, it could be argued that we should broaden what we mean by perception. And we might be left with (conscious) experience. Stretching this definition to the limit, we could even include beliefs, desires, and other seemingly non-sensory experiences as **perception in a broad sense**. 

The lines definitely are blurry. Desire, for example, could be seen as the perception of the sensory process of certain chemicals (hormonones) within our blood. Belief, on the other hand, seems closer to seeing something in a dream in that there are no sensory counter parts. What belief and dreaminf have in common, though, is that they are _experienced_.

_Science_ is the practice of applying logical reasoning and observations to answering questions about the world. 

:::{caution}
:class: dropdown
Do you agree with these definitions? How would you define these terms?
:::

## SCIENCE

There has been an enormous amount of scientific research on sensation and perception. And, just like most science, the outcome of this collective effort has proven _productive_, _effective_, and _beneficial_ - and arguably more so than any other approach to studying sensation and perception. That is, thanks to the *science* of perception, we have become able to successfully help people that we had not been able to help before, such as using cochlear implants to allow people who were born deaf to become able to hear. It is success of this kind that lends strong support to science being worth doing and studying.

:::{attention}
Can you think of other arguments for doing and learning about science?
:::

But what is that - science? Somewhat surprisingly, this is not easy to answer definitely. There is wide general agreement on what we mean by "science", but debate sometimes errupts on where to exactly draw the line. Put simply, we have not managed to find both the _neccessary_ and _sufficient_ criteria that allow us to tell science from non-science. 

:::{important}
Finding the exact criteria that differentiate science from non-science is called the "demarcation problem". Many older textbooks of science suggest that such a criterion has been found by Karl Popper in demonstrating that science can never prove anything, but disprove erroneous assumptions ("faslification"). However, this is not a sufficient criterion since not everything that can be falsified is science. For example, the statement: "Tomorrow you will be the only human alive." can be falsified - you just wait until tomorrow and see if there still are other people alive. However, this does not seem to qualify as science. Another problem is that scientists also seem to struggle to falsify statements. In fact, it may be impossible to falsify statements based on empirical data. New data can always force scientists to revisit what they thought to be the case - including when they thought they had falsified something. Scientists long thought that the view that the "sun goes around the earth" had been falsified and that "the earth goes around the sun" instead. However, Einstein;s theory of relativity demonstrated that neither statement is false. In relativity, both statements are correct, depending on the chosen reference frame - the two views are mathematically equivalent.
:::

But the fact that there may be a bit of gray area at the margins does not take away from the large body of work that most people agree is science. This agreement has a few common denominators:

:::{admonition} WHAT IS SCIENCE?
**Science is a method**: Science is a _principled_ approach to understand the world. Exactly what constitues this method is frequently debated. Yet, there is broad consensus that science as a method starts with a _skeptical_ stance (see next section) in that it aims to find _sound_ answers to questions by sticking to a non-arbitrary, lawful (rigorous), precise and validated (fact-based) approach. If we strip the details, many have suggested, what we find at the heart of science is a constant, perhaps never ending, interplay of rational (logical) reasoning about questions and an attempt of arbitrating between the ideas that arise from this reasoning via empirical observation. That is, science produces ideas (conceptual theories) and then proceeds to match (test) the _consequences_ of these theories (i.e. predictions about what we can observe that arise from these theories) by leaving the armchair and collect data about the world - ideally in well-controlled experiments, and even better using quantitative rather than qualitative predictions and measurements. 

Following observation, we may either gain or lose confidence in our theories given how well their predictions match what we find using these observations. Losing confidence may prompty us to refine our theories, or even abandon them altogether in lieu of new theories that we can then test again observationally. However, even if we gain confidence in our theories, we need to be prepared that additional (future) observations may prompt us to lose confidence at a later point in time. 

Using this bare bones, overly simplistic description of science, we end up with a loop - a constant interplay between theory and observation. However, we are not going in circles. Each time we go around the loop, we seemingly progress in that we can detect flaws in our theories (if they fail to provide a good match between prediction and observation), and thereby arrive at new theories that might allow for better predictions and thus a closer match with what we observe (Figure 2).

**Science starts with (and ends in) doubt**: The cornerstone of science is that _anything can be (and in fact, should be) doubted_. That is, the starting point of science is to not take any statement about the world for granted. Science assumes that _we know nothing for sure_. In other words, science assumes that _everything we know_ is just an assumption. At the same time, science assumes
that _not all assumptions are valid_. Science does not assume that _we know nothing_, or that _we will never know anything_. Instead, science assumes that:
    1. There is one reality, and hence absolute (objective, mind-independent) truth, a completely matching, accurate description, about what this reality is like.
    2. We can gain insight into some assumptions about this reality being _more likely_ than others. In other words, we can make progress in finding assunmption about the world that are very unlikely to be correct, or true.

**Science leverages reason (logic) and observations (empirical/experimental data)**: The scientific method, at its core, consists of a constant interplay, or iteration, between reasoning (theorizing) about the world, and testing consequences (predictions) that arise from these theoretical assumptions. New observations (data) can require theories to be adjusted to the answer that nature provides to our interrogations. And, on the flip side, theories ought to provide new suggestions for empirical tests to probe the theories for their predictive and explanatory power. _This process does not have a defined end point_. Science does not claim that it can ever find truth. All it claims is that we can progress on detecting wrong assumptions of ours, and use that realization to hone and improve on our theoretical assumptions. As the Scientist-Poet said:
    The idea behind science is that **we err. But less and less and less.**
:::

% Bare bones model of the scientific method
:::{figure} images/scientific_method_simplistic.png
:label: fig:simplistic_science_model
:alt: An overly simplistic, bare bones model of the scientific method.
:width: 50%

An overly simplistic, bare bones model of the scientific method.
:::

However, we will not just discuss the science of perception. In fact, nothing we have discussed so far is science (yet). What we have done so far is reasoning that *precedes* science, or meta-science. In other words, we are in the realm of philosophy. 

And there is a bit more philosophy that we need to discuss before we start with the science of perception proper. A lot about what we learn about the science of perception will make more sense after that. In fact, you might want to come back here again often as you progress in learning about the science of perception in order to reevaluate your thoughts on the overarching philosophical questions that we will discuss next.

### Sensation vs. Perception

#### Perception vs. Reality

:::{admonition} DEFINITION
*Naive Realism* is the view that the world is your perception. That is, the world is exactly how you experience it. You feel, see, hear, smell, and taste things exactly as they are. We call this idea "naive" since it seems to reflect the way that children think about the world before they learn why this idea does not seem to work.
:::

:::{admonition} QUESTION
What do you think? Is naive realism correct or wrong? What arguments do you have to defend your view? 
:::

In fact, the starting point of the science of perception is the realization that what we feel, see, hear, smell, or taste is not to be confused with what the world is _actually_ like.

This realization can esily be demonstrated with visual illusions, where we understand that what we _see_ is "wrong" in that our perception deviates from reality of the physical stimulus (Figure 3):

% Lilac Chaser Illusion
:::{figure} images/lilac_chaser.gif
:label: fig:relilac_chaser
:alt: The Lilac Chaser illusion
:width: 80%

The Lilac Chaser illusion[^2]: Keep looking at the center cross and watch the animation changing.
:::

[^2]: https://en.wikipedia.org/wiki/Lilac_chaser

One interesting fact about visual illusions is that they often persist even when exactly understand in what aspects they differ from the actual physical stimulus. In other words, even knowing *that* and *how* our perception differs from the real world does not help - our perception does not correct and adjust to what we know to be really the case.

The consequence of this insight is that there seem to be two different things, or domains that are not identical (since one can deviate from the other): 

1) The physical world consisting of the universe, our local environment, and our own bodies.

2) Our conscious subjective perception of our environment and bodies.

There are many corrolaries from that view, many of which raise deep questions that humanity has not found satisfying answers for yet. 

### Ontology

We talked already about how philosophers call thinking about the limits of what we can know _epistemology_. Thinking about that what  exists is called _ontology_. Together, these two types of thinking form an interplay of that which exists (the ontic) and what we can know about it (the epistemic). Our perception seems to be neither - it is not knowledge and it does not seem to be what really exists, so we call thinking about our perception _phenomenology_.

Naive realism, in a way, is a simple epistemology where phenomenology is equated with ontology, Realizing that we do not perceive the world as it is leads to a more sophisticated epistemology that differentiates between our phenomenology and ontology. But what can we know about ontology? Metaphorically speaking, if our phenomenology is akin to the shadows seen by the prisoner's in Plato's Cave, how can we find out what is actually going on outside the cave?

If naive realism is problematic, which other worldviews are there that might be more convincing? You might immediately think about science, especially since we argued for its strength above. And, indeed, the scientific worldview differs widely from naive realism. However, as we will see, there actually are a large variety of very different worldviews that all claim to be compatible with science. And many of these diverging worldviews that base themselves off science differ in how they think about perception!

% The scientific worldview
:::{figure} images/scientific_view.png
:label: fig:scientific_view
:alt: The scientific worldview
:width: 90%

The scientific worldview. Rather than equating our perception with the world, scientists see the world as a complex dynamic system following mathematical laws, much of which is not directly perceived, and some of it not perceivable at all. The challenge then becomes to _explain_ how the world of our perception relates and comes about from the physical world. 
:::


#### Do we all perceive the world differently? 
If our perception is different from the world (i.e., what and how we perceive things is not the same as the physical reality of these things), the question arises if each of us perceives the world _differently_. 

:::{admonition} QUESTION
Ask yourself: Is it possible that what I call "red" in fact might look to me like what you call "green"? If I would see green where you see red, would we ever be able to find that out? How? 
:::

As we will see, the answer is a bit mixed. There are, of course, individual differences in, say, how we perceive color since some of us are what we colloquially call "color blind" (we will see why this is a misleading term). However, as we go along, we will see that we generally seem to perceive very much alike. 

:::{admonition} QUESTION
Is it surprising that most of us seem to perceive colors similarly? Why does that or does that not surprise you?
:::

#### If our perception can be misleading, how can we know what the world is actually like?
Another puzzle that arises from our realization that we can fall pray to perceptual illusions is that this seems to put into question how we can _know_ that to be the case. DO we only know the world only from our perception? How else can we learn about the world? Can we know for certain that there really _is_ a world "outside" our perception?

This line of questioning may seem ludicruous at first. We all seem to agree that there is a "real world out there". How could this be questioned? And, at first, there does not seem to be a problem to know what that world _is like_. Is that not what physics and other sciences do - tell us what the world "really is", even if different and independent of our own perception?

But deeper reflection makes clear that this is not, in fact, so easy. Let us unpack that.

##### PLATO'S CAVE
You might have heard about Plato's allegory of the cave. In this ancient ficticious story, a group of people is held hostage inside a cave. They grew up there and never were able to step outside. In fact, these people do not even know that there is an outside. Since they grew up inside that cave, they have no reason to believe that the world is much more than that one place - the only place - that they know Plato wants us to imagine what things would be like for these people. 

Plato goes on that we should imagine that these people are chained to a wall so that they cannot turn around and see what is behind them. Again, he asks us to just imagine the scenario and put ourselves into the shoes of these people to make an interesting point.

He then goes on to describe that there is gap in the walls of that cave - a window of sorts. Light falls through that gap and the people that grew up inside that cave can only see that light on a wall opposite to that opening.

Here comes the kicker: Plato now describes that the people inside the cave can sometimes see shadows on that wall that is illuminated by the gap behind them. Now, imagine that you are one of the people that grew up in that position. For you, the shadows cannot be understood as shadows. That is, because you have no concept of shadows. You just see sillhouettes opposite to you. They are part of your world. They are "real" to you as much as anything else inside the cave.

Plato's story goes on, but the key insight can already be made here. Plato makes clear that the people inside the cave could be fooled, for example, by people on the outside purposefully walking cut-outs made of paper or would along the gap behind the people inside the cave and create a "shadow theater" for the people inside, like we sometimes do for young kids. There is no way to know for the people inside the cave that the shadows they see are just artificially created by people outside - since they do not know that what a shadow is, that there is an outside, let alone people that are outside.

What does any of that have to do with perception? Well, one corollary of us establishing that
1) There is a real world "outside" our perception
2) Our perception seems to be more like a reflection, or "shadow" of that world
is that we are in a similar position as these people inside the cave: We only know the "shadows", a reflection, of the world and not the world itself. Our skulls, our brains, seem to be similar to that cave in that our perception arises from "inside" these structures. 

Finding out what the real world, that is responsible for the "shadows" of our perception, is actually like then seems to become challenging: We have to _reason_ about what this world might be like since we cannot go by our perception alone.

This may still sound a bit confusing at this point. After all, we have not talked about what role our brains play in all of that (and since brains are obviously also part of that world that we perceive). We all share to some degree the notion that our brains are linked to our feelings, our ability to see, hear, smell, or taste. But what we will learn soon is _how closely_ linked the actions of our brain are to what we perceive. For now, it is only important to follow the logic of Plato's allegory: _If_ our direct acquintance with the world is our perception, and that perception can be unreliable (as in the sxistence of illusions), the problem arises that we have to find additional ways other than our perception to learn about the world.

##### PERCEPTION vs. WORLD
Many thinkers that followed Plato have thought deeply about this issue. However, they failed to all settle on the same solution. Instead, these scholars have endowed us with a variety of ways to think about that problem, each arguing for their favorite idea. Let us briefly (and superficially) examine the various proposed answers. The academic field that studies these ideas is called _PHILOSOPHY OF MIND_, and there are thousands of academic works on this subject. Here we will attempt at the most minimal possible overview of major "schoolf of thought" within this field:

###### MONISM
One possible solution is that there really is only one thing. That is, the assumption that we had that there is a world and our perception of the world is wrong. This leaves only two options: All is the world (i.e., there is no perception), or all is perception (there is no world).

The actual ideas are a bit more complex, but they do not deviate far from the sentence above. The technical terms we use for these ideas are:

*MATERIALISM*: There is only the world. There is no perception. If you think that you perceive something, what really happens is that you _behave_ or _function_ according to what you call a perception (which is why this view is sometimes also called **BEHAVIORISM** or **FUNCTIONALISM**). You thinking that you perceive things beyond behaving and functioning according to physics, is _illusory_. You _believe_ you perceive, say the color "red", but that is a false belief. You just act as if you do. Some proponents of this view prefer the term "physicalism" to demonstrate that they agree with modern physics in that "matter" is not a substance (modern physics describes matter as "an interaction" between the Higgs field and other quantum fields, but you do not need to worry that you need to know about all of this).

*IDEALISM*: There is no physical world. All is perception (again, technically, proponents of this view would use broader terms like "mind", or "consciousness" - but it is debatable how much these concepts do or do not overlap). There are two options on this view:

    **SOLIPSISM**: Your perception is all that exists. Nothing else is real. You are all alone. Everything is just an illusion, except your perception. This view is difficult to argue with rationally. At the same time, view people are convinced by this view, let alone prefer this view since it resembles a horrifying reality.

    **PANPSYCHISM**: Everything is perception. This view grants that there is "a world out there", but it assumes that that which exists outside our own perception is even more perception - a grand ocean of perception, if you will. Proponents of this view suggest that something keeps our own perception separate from the rest of perception out there.

###### DUALISM
Another possible solution is that there really are two different things: a world and our perception. But there are some disagreements on what exactly makes them different.

**SUBSTANCE DUALISM**: This view, often credited to René Descartes, even though it can be found in many (older) cultures around the world is that your perception is real, yet "immaterial". And that the world is "material", or physical. Proponents of this view try to explain why and how these two domains are linked, such as how (material) brain damage or intoxication can alter (immaterial) perception. On this view, (immaterial) perception might also be able to affect the (material) world.

**ASPECT DUALISM**: This idea takes a bit of a middle ground. It does assume that there "really" only is one thing, and thus subscribes to monism. However, it suggests that one and the same thing can have different aspects, or properties when viewed from different percectives - somewhat like a coin can look very different if one only looks at heads or tails. Aspect dualism assumes that there is a real world that may well be physical, but that our perception is what some physical systems, like our brains, _are like_ from the "inside". This view explains why brain damage can affect perception since they are just "two sides of the same coin". 

There are many more ideas on that problem, some of which cannot neatly placed within the taxonomy above. However, these cateogories provide a somewhat of a sufficient survey of the field since most ideas come close to, or combine, these distinct schools of thought. To give you an example, some scholars will state that they are "_REDUCTIONIST PHYSICALIST_", for example. A popular version of this view is that "there is only the physical universe" and that perception "emerges" from some physical system in a way that can be explained by physical laws. Note, how this notion comes close to our option of _ASPECT DUALISM_.

:::{admonition} QUESTION
WHICH OF THESE IDEAS BEST DESCRIBE YOUR OWN VIEW? WHY DO YOU DISMISS THE OTHER VIEWS?
:::

For the purpose of this course, we will adopt a somewhat neutral dualistic stance. That is, we will base our knowledge about the world on the atural sciences such as physics, chemistry, and biology. At the same time, we will treat perception as a real phenomenon that goes beyond its behavioral or functional corrolaries. At the end of the semester, we will re-examine this view, and discuss how what we learned can also be applied to other views. As we will see, the scientific knowledge that we will gain will end up as largely compatible with _most_, if not all, of these views. At the same time, you will have learned new facts and logical insights that pose challenges to each of these views, thus making it even more interesting to ponder about their validity.

## MATHEMATICS 

When we think about science, including biology, geology, chemistry, and especially physics, we tend to also think about mathematics. In fact, we seem to be rarely taken aback when we encounter physics in a lecture or a textbook and _most_ of what we are confronted with is mathematics. 

% Math and Physics
:::{figure} images/wiki_physics.png
:label: fig:wiki_physic
:alt: Math and Physics
:width: 70%

The _wikipedia_ entry on "Physics" shows a mathematical diagram under "Scopes and Aims".
:::