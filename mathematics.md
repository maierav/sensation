# MATHEMATICS

% Newton The Geometer
:::{figure} ./images/newton.jpg
:label: fig:newton
:width: 70%

William Blake's Newton as a Geometer (1795).[^1]
:::

[^1]: [public domain source](https://commons.wikimedia.org/wiki/File:Newton-WilliamBlake_crop.jpg)

Science rests on mathematics, so we cannot completely avoid the topic. The following is a brief refresher for the (very limited) mathematics that we will use later on this course. We will start by assuming zero knowledge about mathematics, and then built up quickly from there. If you feel, at any step, that we moved to quickly, this may signify that there is need to brush up a bit via self-study. A few, hopefully helpful, sources and references are provided to do just that.  

    No calculations required.

As we already discussed, due to our schooling, we tend to think of mathematics as calculating, or resolving equations. This can turn since into a competition of sorts, where there is a correct solution (that an "authority" such as a teacher or a textbook author) knows and we can either fail or succeed in finding out. We will do none of that. Instead, we will ponder a bit more about the fundamental assumptions and operations that _underly_ this process. The goal is still to read and understand mathematical formalism and descriptions, but with a focus on _meaning_ (the information contained within) rather than computing or deriving a correct outcome by ourselves. Hopefully, this will also allow you to see mathematics "in a new light", and add a bit of _fun_, or at least make it all seem a bit more _interesting_.  

## FOUNDATIONS

% Math
:::{figure} ./images/math.jpg
:label: fig:math
:width: 55%

Mathematics has been taught to students for thousands of years.[^2]
:::

[^2]: public domain sources: [1](https://commons.wikimedia.org/wiki/File:Acta_Eruditorum_-_II_geometria,_1707_%E2%80%93_BEIC_13369403.jpg), [2](https://commons.wikimedia.org/wiki/File:Acta_Eruditorum_-_I_geometria,_1715_%E2%80%93_BEIC_13386284.jpg)

We already discussed that modern mathematics starts with one or more _axioms_ that one has to accept without further questioning. So, what are the axioms that underly _all_ of mathematics (or, since one can always drop or add axioms and thus change mathematics, the largest body of mathematics)?  

### Set theory

The currently most commonly considered axiomatic foundation of mathematics is **set theory**, specifically the _Zermelo–Fraenkel_ set theory with an additional axiom (the _Axiom of Choice_), abbreviated as **ZFC**.  

You might now wonder: "How many axioms will I need to accept as a foundation of mathematics?". In other words, what is the minimal number of axioms that we can reduce the theorems of a large body of mathematics to? What is the number of axioms that make up ZFC?  

The answer is (in the most common formulation): 9.  

No worries - we will not have to go over all of these axioms. Instead, we will just take note, ponder for a moment whether this number of axiom seems surprisingly high or low, and move on. What we really want to do is take a brief look at the most basic "picture" that set theory provides and use it to get a sense of what we mean by "number" (yes, we will keep it that simple). Then we will see what we can _do_ with numbers, resulting in basic **arithmetic** (addition, subtraction, multiplication, and division). After we discussed _exponentiation_ and _logarithms_, we will be largely done.  

You might feel that you understand all these things already, so why bother? In fact, we will assume that you already do. However, remember that we started out with _radical doubt_, and deriving some certainty from a combination of experience and logic. We also started out by striving for _coherentism_ in our knowledge in probing for the possibility of a unified whole of science. We thus need to explore whether mathematics, which might have been taught to us as an isolated fragment of knowledge fits in our _singular_ approach that we have started. In other words, you probably already know much more about numbers, addition, and even logarithms than we discuss here, but we will aim to look at them from a perspective, a new light perhaps, that unifies all them in some sense rather than a diverse set of lenses that we have to choose from and wear one-at-a-time.  

There is, fo course, a lot to say about ZFC. The Axiom of Choice, for example, is highly contentious. There is also an alternative proposal for a foundation of mathematics called **category theory**. We will consider the difference between these two starting points of mathematics in a bit since it might be relevant for how we approach mathematics in the context of perception. But for now, let us stick to set theory since - as you will see - it can help us to somewhat intuitovely derive the basic mathematics we require.  

## Numbers

    Ask three mathematicians what a number is. 
    You’ll get five definitions.
    And all of them will be correct.

Now that we have gained a (very) basic understanding of set theory, which we identfied as the foundational basis of much of mathematics, we can explore the concept of numbers. "Why just now?", you might wonder. After all, (pre-)school mathematics tends to start with numbers, and builds from there, often teaching set theory at a much later stage.  

However, we needed to start from _foundations_, and numbers are commonly derived by modern mathematics using the axioms of set theory (ZFC). More so, since we already are at a point where we ponder things more deeply, numbers are not as simple as they look at first sight. Thinking about numbers (deeply) can quickly turn puzzling. And having set theory as a backdrop can help prevent a bit of that.  

### Arithmetic

Now things get really interesting. Numbers by themselves just seem to "exist" and "not do anything". And when we were young, we probably quickly realized that numbers really show their usefulness once we add, subtract, multiply, or divide them.  

And all of that seems to come quite naturally. After all, we can do the same thing with concrete objects: add one apple to two others, divide a pizza in half, and so on.  

But things can become a bit confusing, or non-intuitive rather quickly:

**Addition** allows us to disregard order: 2 + 4 is the same as 4 + 2. Both is 6.  

    4 + 2 = 2 + 4

The fancy word for this property of addition is **commutativity**.

This small observation is worth pausing for. What is that? What does that mean that we can disregard order in this way? This is clearly not _always_ the case:  

If you pick up a book so that you look at its cover, and then _rotate forward_, and you now look at the bottom of the book. Now you _rotate to the left_, and you will look at the side of the book, and see all its pages.  

But if we start again by wlooking at the book's frontcover, and then you _rotate to the left_, you will look at the side of the book and see all its pages. Then _rotate forward_, so that we reversed the sequence in which we perform the operation. But now you do do not see all of the books pages on one of its sides, like you did before. Instead, you look at its bottom.

So, rotating a book does not _commute_. You cannot just change the order and end up with the same outcome. Tbus it is worth noting that addition of whole numbers _is_ commutative in that we can reverse the order of which number we add to the other. Either way, we end up with the same sum.  

One way to think about this (trivial seeming) "rule" of commutativity is that this seems a bit different from what we usually think about when we think about "mathematics". That is, we all understand that adding to numbers and findning out their sum _is_ mathematics. We might even include the _numerals_ that _symbolize_ the numbers (such as '5') and the symbol that stands for addition (+) as "mathematics". But all of these are _human-made_. We calculate, come up with, and write the symbols etc.

But commutativity (the _fact_ that we can reverse the order of numbers we add and still get the same result) seems a bit different. Something a bit more "hidden". And less _human-made_. It just seems like we "discovered" that when we calculate, or even when we add physical objects together, this process is _guided_, or ruled by, commutativity. To many mathematicians, this is very interesting. They refer to this "discovery" of underlying rules as "mathematics" as well. But since it seems not quite the same as the _activity of doing mathematics_, we might want to refer to it with a different noun, such as **the mathematical**. The mathematical is what we _describe_ when we _do_ mathematics. Or, put differently, the mathematical is that which mathematics _studies_. It is the _subject_ of mathematics (and hence, not the same as mathematics). This distinction can be helpful as we continue to ponder a bit more about what, how, and why mathematics will play a key role in our exploration of perception.  

**Subtraction** seems to be a simple inverse process. We just reverse what we just did.  

Let's say we added 2 apples to 4 apples:

    2 + 4 = 6

We can just take these 2 apples away again. Undo addition - and get subtraction:  

    6 - 2 = 4

But if this subtraction is basically the same as addition, just the other way around, a kid who discovers all might be surprised that there is a big difference: Subtraction is not commutative.

    6 - 4 = 2

Indeed, many people feel that addition is a bit more "easy" than subtraction. And the fact that additivity is a bit more "lax" in that you disregard order while subtraction requires you to make sure that you do not accidentally confuse the order might be part of that reason.  

For now, all we should do is put an earmark in this very simple observation. Arithemtic seems easy since we can think of subtraction as the inverse of addition. And yet, there is an added bit of complexity in that these two operations are not quite as fully _symmetric_ as it seems. Different rules apply for each.  

_While addition is commutative, its inverse (subtraction) is not._

And there is another reason why students often find addition more "intuitive", or "easy" than subtraction: Subtraction often is where we learn that there are more than the _whole numbers_ (1, 2, 3, 4, ...).  

First, we might get confronted with 0:

    5 - 5 = 0

0 expands the _while numbers_ (1, 2, 3, ...) to the _natural numbers (0, 1, 2, 3, ...). Few adults worry about that fact, but zero is not a trivial concept and it took humanity a long time in history to accept it as mathematically valid. After all, _nothing_ just seems to be "absence of anything", so how can there - how can it - be _something_, like zero?  

But subtraction leads us deeper:

    5 - 7 = -2

Now, we need to expand our concept of numbers once more. And we end up with _integers_ (..., -3, -2, -1, 0, 1, 2, 3, ...). Again, most adults have become used to the concept to negative numbers, but for a kid this is another challenging concept: "How can there be _less_ than _nothing_?"

All of this is just to remind ourselves that there are (minor) conceptual obstacles and counter-intuitive notions amidst some of the most basic math. And becoming aware of that can be helpful both for re-grounding and re-convincing ourselves that we had good reason to accept these notions, and that we should be careful in shrugging off math that we have become very used to as "trivial".  

In fact, it could be argued that some of these conceptual challenges, as small as thy may seem_ are actually _larger_ than what we face at higher levels of mathematical abstraction. And - if we were struggling with some of these conceptual hurdles (such as: _what could be smaller than nothing_) at first when we were taught basic mathematics, we hopefully did not just "accept" these notions and move on. Doing so risks that we start to just "trust" mathematics and what people who are more educated in mathematics tell us rather than doing that which mathematics offers and demands: not to trust, but to convince yourself through reasoning. So let us keep doing just that.  

 Let us move on to **multiplication**. [Yes, this slow walk may seem a bit silly, but keep going. There is a bigger point we will get to in a moment.]

One way we might have been taught multiplication is to treat it as something _entirely_ different than addition (or subtraction). This is often done by learning "by heart" (akin to a poem) a _multiplication table_ so that we can immediately recall the answer to something like:

    5 * 5

We _learned_ that the solution is:

    5 * 5 = 25

Of course, that is not all. We also learned that we can convince ourselves that the multiplication table is correct by just performing the calculation by ourselves, such as counting 5 times to five and adding all up.  

And here in lies the key: We can find out what the outcome of multipication is by _adding_:

    5 + 5 + 5 + 5 + 5 = 25

So, at least in this sense, we can think of multiplication almost as a "shorthand" for _repeated addition_:

    5 + 5 + 5 + 5 + 5 = 5 * 5

It's just "less to write", if you will.

Now, deeper thought about multiplication leads us elsewhere. There is actually something more interesting about what a (Cartesian) **product** is. It is a unique kind of combination, in fact. But for our current context, it is more helpful to grasp that there is a _link_ between addition (which many feel is relatively "easy" to do) and multiplication (which "feels" a bit more involved; partly because we quickly end up with much larger numbers).  

Now - what about division?  

Well, we can think of it as the _inverse_ to multiplication, of course. In a sense, it is simply undoing what multiplication does:

    25 : 5 = 5

And, once again we find: _While multiplication is commutative, its inverse (division) is not._  

This asymmetry, here too, may be why students often find division a bit more challenging than multiplication. But there is an added reason: Division is where often are first introduced to numbers that are not _natural numbers_.  
