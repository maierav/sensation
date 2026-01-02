# MATHEMATICS

% Newton The Geometer
:::{figure} ./images/newton.jpg
:label: fig:newton
:width: 75%

William Blake's Newton as a Geometer (1795).[^1]
:::

[^1]: [public domain source](https://commons.wikimedia.org/wiki/File:Newton-WilliamBlake_crop.jpg)

Science rests on mathematics, so we cannot completely avoid the topic. The following is a brief refresher for the (very limited) mathematics that we will use later on this course. We will start by assuming zero knowledge about mathematics, and then built up quickly from there. If you feel, at any step, that we moved to quickly, this may signify that there is need to brush up a bit via self-study. A few, hopefully helpful, sources and references are provided to do just that.  

    No calculations required.

As we already discussed, due to our schooling, we tend to think of mathematics as calculating, or solving equations. This can turn since into a competition of sorts, where there is a correct solution (that an "authority" such as a teacher or a textbook author) knows and we can either fail or succeed in finding out. Here we will do none of that. Instead, we will ponder a bit more about the fundamental assumptions and operations that _underly_ this process. We will "figure things out" by "connecting the dots". And by examining the resulting structure, we hope to find (literal) _insight_, as in seeing "math from the insde" or "what lies inside".  

% Flammarion
:::{figure} ./images/flammarion_colored.png
:label: fig:flammarion
:width: 80%

The Flammarion engraving provides a metaphor for mathematization in science: Empirical observation corresponds to the contingent, and perspectival that we are all familiar with. Mathematical structure corresponds to what lies beyond: invariant, non-perspectival. Mathematics strips away observer-specific phenomena and produces observer-invariant _relations_. Math provides statements that are unaffected by who observes, where, or when. In this sense, mathematics is not one science among others — it is the means by which science escapes subjectivity and achieves explanatory unification.

Using mathematics, science seemingly crosses the empirical horizon to access structure that is not itself observable, such as Hilbert spaces, manifolds, groups, probability measures, causal graphs. While debated, scientist seem unlikely to merely _invent_ this underlying structure, but seemingly _discover_ it when describing an underlying abstract order that is not readily apparent in ordinary observation (unknown artist, 1888).[^2]
:::

[^2]: [public domain source](https://commons.wikimedia.org/wiki/File:Colourflamarion33.jpg)

To put it a bit more high brow: We will focus less on _mathematics_, the _human_ (mind-dependent) activity that leads to symbols (notation), proofs, calculations and equation solving. What the following aims to instill is to, in some sense, look past all that and focus on what all that _describes_. The _structure_, the laws, rules, order, or patterns that all this points to, or follows. Following P. Freyd, we will call this **subject of mathematics** the **mathematical**. If you see mathematics as a _language_, then the mathematical is that which this languages describes.  

[So, even is you already feel quite familiar, or well-versed, with the topics of this chapter (starting with basic arithmetic and leading up to logarithms), you are well advised to nonetheless read along. In fact, much of what follows assumes that you already know what, say, addition is. The emphasis is elsewhere - seeing addition in a "new light".  

Ask yourself: How does the logarithm relate to addition?

There is a simple, fascinating, and structurally deep relation between these two operations that are conventionally taught in a somewhat isolated, successive manner. Grasping this relation might be a more intuitive, easier to understand and appreciate, manner of getting familiar with logarithms. And logarithms are a key step to understand the (neuro)science of perception.]

The goal is still to read and understand mathematical formalism and descriptions, but with a focus on _meaning_ (the information, the _structure_, contained within) rather than computing or deriving a correct outcome by ourselves. Why compete with machines, such as pocket calculators, that are much better at that? It seems more fruitful to instead focus on those aspects of mathematics that machines struggle with - exploring and understanding how mathematics interconnects and forms a cohesive whole. Hopefully, this will also allow you to see mathematics "in a new light", and add a bit of _fun_, or at least make it all seem a bit more _interesting_.  

## FOUNDATIONS

% Math
:::{div}
:class: hidden dark:block

:::{figure} ./images/math_dark.jpg
:label: fig:math
:width: 65%
Mathematics has been taught to students for thousands of years.[^3]

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/math.png
:label: fig:math
:width: 65%
Mathematics has been taught to students for thousands of years.[^3]

:::

[^3]: public domain sources: [1](https://commons.wikimedia.org/wiki/File:Acta_Eruditorum_-_II_geometria,_1707_%E2%80%93_BEIC_13369403.jpg), [2](https://commons.wikimedia.org/wiki/File:Acta_Eruditorum_-_I_geometria,_1715_%E2%80%93_BEIC_13386284.jpg)

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

So far we mostly discussed (or looked at) _geometric_ descriptions of math. Historically speaking, this makes sense since we established that modern axiomatic mathematics finds it origin in ancient Greece with Euclid. But just a brief look at Stonehenge leaves us with the impression that geometry has fascinated humans for much longer (at least all the way back to the _stone age_).  

% Stonehenge
:::{figure} ./images/stonehenge.jpg
:label: fig:math
:width: 85%
Stonehenge is aligned with the sun's position during the solstices.[^4]
::

[^4]: [public domain source](https://commons.wikimedia.org/wiki/File:Acta_Eruditorum_-_II_geometria,_1707_%E2%80%93_BEIC_13369403.jpg)

One cannot help but wonder whether part of this fascination with geometry is partly rooted in its relation to _measurement_ (of astronomical events, such as the solstice) as well as in the fact that it is _tangible_. That is, a Euclidian geometric proof does _not_ just exist in the "abstract". Instead, we can convince ourselves that the proof "works" in the real world by using a compass and a ruler and literally draw out the proof (the various operations) on sand, a blackboard, or a piece of paper.  

But if it was pragmatic _usefulness_ (e.g., for predicting the solstice or delineating a piece of land that is under dispute between two farmers) that led to the study of geometry, we quickly come to appreciate a seemingly _separate_ part of mathematics: counting, calculating - using **numbers**. From a pragmatic standpoint, numbers become relevant the moment we think of _currency_, or money. Salaries, debt, wealth all needs to be handled by using numbers (nobody is surprised to find numbers when taking a look at their credit card bill or bank account).  

When it comes to the science of perception, then, we need to take a look at both - geometric structurs and numbers. An obvious question, after all, is that - if we want to be precise and mathematize - the science of perception in order to make it "as scientific" as, say, physics, which mathematics does best apply? Is it geometrical, structural descriptions or numerical measurement and description?  

As we will see, these two seemingly _distinct_ fields of mathematics have long been _unified_,  

:::{admonition}
:class: dropdown
:open: true
Do you know by whom?
:::  

:::{tip}
:class: dropdown
Descartes. And this won't be the last time that we will encounter him.
:::

But, we can leave that aside for the moment, and take a closer look at what made _numbers_ seem so separate from the study of geometric _structure_ (again, luckily, Descartes and others demonstrated that we do not really have to choose one over the other). There is something peculiar about numbers in that it becomes more challenging to point to physical objects, like Euclid did for his geometrical proofs. Numbers can seem more "abstract", or, on some people's view: mind-made.  

:::{admonition}
What can we point to in the real world to explain the number zero? Or the number -1?  
:::

In fact, it tends to be the discovery of numbers, such as the square root of 2 where students first encounter a nagging feeling (most of that have forgotten that this happened when we were young). And that feeling has justification. There is something non-trivial about a number, such as the square root of 2, allowing mathematicians to abandon precise calculations, and instead just "round up" or "approximate" (or just stick to a symbol) as a _correct answer_. This _is_ confusing. And by brushing over the confusion that arises at that point of learning mathematics can give rise to the feeling of "**not being good at math**" and eventually "**not liking math**".  

Much of what follows aims to remedy this problem. And in order to do so, we will slowly and carefully go over elementary and middle school (as well asperhaps some high school, depending on modern corricula) mathematics again and stop whenever we encounter these moments of potential, justifiable, confusion. It may seem silly to discuss addition of, say 2 + 3 again, but stick with it. It is likely that you will learn something new. And at the same time get a better feeling that while 2 + 3 seems "easy" or even "trivial", taking the logarithm of 34 does not. But, if we succeed, it becomes clear there is a clear and surprisingly simple connection between the two operations. And then the notion of "easiness" that comes with addition of 2 and 3 hopefully will extend to taking the logarithm of 34. Or pondering a bit about the square root of 2.  

So, now that we have gained a (very) basic understanding of set theory, which we identfied as the foundational basis of much of mathematics, we can explore the concept of numbers. "Why just now?", you might wonder. After all, (pre-)school mathematics tends to start with numbers, and builds from there, often teaching set theory at a much later stage.  

However, we needed to start from _foundations_, and numbers are commonly derived by modern mathematics using the axioms of set theory (ZFC). More so, since we already are at a point where we ponder things more deeply, numbers are not as simple as they look at first sight. Thinking about numbers (deeply) can quickly turn things puzzling. And having set theory as a backdrop can help prevent a bit of that.  

### Arithmetic

Now things get really interesting. Numbers by themselves just seem to "be made up" and "not do anything". And when we were young, we probably quickly realized that numbers really show their usefulness once we add, subtract, multiply, or divide them.  

And all of that seems to come quite naturally. After all, we can do the same thing with concrete objects: add one apple to two others, divide a pizza in half, and so on.  

But things can become a bit confusing, or non-intuitive rather quickly:

**Addition** allows us to disregard order: 2 + 4 is the same as 4 + 2. Both is 6.  

$$
  4 + 2 = 2 + 4
$$ (1)

The fancy word for this property of addition is **commutativity**.

% Math
:::{div}
:class: hidden dark:block

:::{figure} ./images/sum_dark.jpg
:label: fig:math
:width: 65%
Summing does not care about the order of operations.[^3]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/sum.png
:label: fig:math
:width: 65%
Summing does not care about the order of operations.[^5]
:::

[^5]: [public domain source](https://commons.wikimedia.org/wiki/File:Green_Apple_Icon.png)

This small observation is worth pausing for. What is that? What does that mean that we can disregard order in this way? This is clearly not _always_ the case:  

If you pick up a book so that you look at its cover, and then _rotate forward_, and you now look at the bottom of the book. Now you _rotate to the left_, and you will look at the side of the book, and see all its pages.  

But if we start again by wlooking at the book's frontcover, and then you _rotate to the left_, you will look at the side of the book and see all its pages. Then _rotate forward_, so that we reversed the sequence in which we perform the operation. But now you do do not see all of the books pages on one of its sides, like you did before. Instead, you look at its bottom.

So, rotating a book does not _commute_. You cannot just change the order and end up with the same outcome. Tbus it is worth noting that addition of whole numbers _is_ commutative in that we can reverse the order of which number we add to the other. Either way, we end up with the same sum.  

One way to think about this (trivial seeming) "rule" of commutativity is that this seems a bit different from what we usually think about when we think about "mathematics". That is, we all understand that adding to numbers and findning out their sum _is_ mathematics. We might even include the _numerals_ that _symbolize_ the numbers (such as '5') and the symbol that stands for addition (+) as "mathematics". But all of these are _human-made_. We calculate, come up with, and write the symbols etc.

But commutativity (the _fact_ that we can reverse the order of numbers we add and still get the same result) seems a bit different. Something a bit more "hidden". And less _human-made_. It just seems like we "discovered" that when we calculate, or even when we add physical objects together, this process is _guided_, or ruled by, commutativity. To many mathematicians, this is very interesting. They refer to this "discovery" of underlying rules as "mathematics" as well. But since it seems not quite the same as the _activity of doing mathematics_, we might want to refer to it with a different noun, such as **the mathematical**. The mathematical is what we _describe_ when we _do_ mathematics. Or, put differently, the mathematical is that which mathematics _studies_. It is the _subject_ of mathematics (and hence, not the same as mathematics). This distinction can be helpful as we continue to ponder a bit more about what, how, and why mathematics will play a key role in our exploration of perception.  

One last thing - we need to also agree on (or accept) precise word for _describing_ the various parts of addition (summation). You probably already know that the number that results from addition is what we call the **sum**. We just need names for the other numbers as well. Since their order does not matter (we can rotate their position and the sum remains the same), we can just use one and the same name for these numbers: **addend**. Adding two addends results in the sum. So, the common definition is:

```{math}
  addend + addend = sum
```

**Subtraction** seems to be a simple inverse process. We just reverse what we just did.  

Let's say we added 2 apples to 4 apples:

$$
  2 + 4 = 6
$$

We can just take these 2 apples away again. Undo addition - and get subtraction:  

$$
  6 - 2 = 4
$$

% Addition and Subtraction
:::{div}
:class: hidden dark:block

:::{figure} ./images/addition_dark.png
:label: fig:addition
:width: 45%
Addition and Subtraction are **inverse operations**.

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/addition.png
:label: fig:addition
:width: 45%
Addition and Subtraction are **inverse operations**.

:::

But if subtraction is basically the same as addition, just the other way around, a kid who discovers all might be surprised that there is a big difference: Subtraction is not commutative.

$$
  6 - 4 = 2
$$

As a result, we have to be a little be more careful for the words we use to describe these numbers:

$$
  minuend - subtrahend = difference
$$

Indeed, many people feel that addition is a bit more "easy" than subtraction. And the fact that additivity is a bit more "lax" in that you disregard order while subtraction requires you to make sure that you do not accidentally confuse the order might be part of that reason.  

For now, all we should do is put an earmark in this very simple observation. Arithemtic seems easy since we can think of subtraction as the inverse of addition. And yet, there is an added bit of complexity in that these two operations are not quite as fully _symmetric_ as it seems. Different rules apply for each.  

_While addition is commutative, its inverse (subtraction) is not._

And there is another reason why students often find addition more "intuitive", or "easy" than subtraction: Subtraction often is where we learn that there are more than the _whole numbers_ (1, 2, 3, 4, ...).  

First, we might get confronted with 0:

$$
  5 - 5 = 0
$$

0 expands the _while numbers_ (1, 2, 3, ...) to the _natural numbers (0, 1, 2, 3, ...). Few adults worry about that fact, but zero is not a trivial concept and it took humanity a long time in history to accept it as mathematically valid. After all, _nothing_ just seems to be "absence of anything", so how can there - how can it - be _something_, like zero?  

But subtraction leads us deeper:

$$
  5 - 7 = -2
$$

Now, we need to expand our concept of numbers once more. And we end up with _integers_ (..., -3, -2, -1, 0, 1, 2, 3, ...). Again, most adults have become used to the concept to negative numbers, but for a kid this is another challenging concept: "How can there be _less_ than _nothing_?"

All of this is just to remind ourselves that there are (minor) conceptual obstacles and counter-intuitive notions amidst some of the most basic math. And becoming aware of that can be helpful both for re-grounding and re-convincing ourselves that we had good reason to accept these notions, and that we should be careful in shrugging off math that we have become very used to as "trivial".  

In fact, it could be argued that some of these conceptual challenges, as small as thy may seem_ are actually _larger_ than what we face at higher levels of mathematical abstraction. And - if we were struggling with some of these conceptual hurdles (such as: _what could be smaller than nothing_) at first when we were taught basic mathematics, we hopefully did not just "accept" these notions and move on. Doing so risks that we start to just "trust" mathematics and what people who are more educated in mathematics tell us rather than doing that which mathematics offers and demands: not to trust, but to convince yourself through reasoning. So let us keep doing just that.  

 Let us move on to **multiplication**. [Yes, this slow walk may seem a bit silly, but keep going. There is a bigger point we will get to in a moment.]

One way we might have been taught multiplication is to treat it as something _entirely_ different than addition (or subtraction). This is often done by learning "by heart" (akin to a poem) a _multiplication table_ so that we can immediately recall the answer to something like:

$$
  5 * 5
$$

We _learned_ that the solution is:

$$
  5 * 5 = 25
$$

The reason for us not _actually_ calculating the result of this equation in our head, but just recall from memory, is quite interesting. It seems to be _not_ a limitation of mathematical _ability_. Instead, it find its root in our _perception_. In particular, we can easily look at a small amount of objects and determine their **quantity** - and thus assign a number. However, the more objects there are, the harder this gets. As we will see in the next chapter, this is one of the most fundamental insights not about mathematics, but about _perception_. And yet, this perceptual limitation, or property, affects our approach to some of the most basic mathematics, such as addition and multiplication.  

% Large Numbers
:::{div}
:class: hidden dark:block

:::{figure} ./images/large_numbers_dark.png
:label: fig:times table
:width: 100%
_**LEFT**_: Our perception of large _quantities_ is very different from our perception of small numbers of objects. When we see two, or three objects, we do not have to _count_ them. We are immediately able to assign a number to their _amount_. However, once we look at ~7 or more objects, this immediate recognition of _numerosity_ becomes challenging, if not impossible. At that point the number of objects starts looking _too similar_ (e.g., 8 or 9 objects _looks_ almost the same). We thus are forced to slow down and start _counting_, which is prone to mistake. _**RIGHT**_: As a result of our experiental limitation of immediately perceiving quantity accurately, we need to _memorize_ the outcome of composing (combining) or decomposing large quantities, such as in the form of a _multiplication table_ (or _times table_).

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/large_numbers.png
:label: fig:times table
:width: 100%
_**LEFT**_: Our perception of large _quantities_ is very different from our perception of small numbers of objects. When we see two, or three objects, we do not have to _count_ them. We are immediately able to assign a number to their _amount_. However, once we look at ~7 or more objects, this immediate recognition of _numerosity_ becomes challenging, if not impossible. At that point the number of objects starts looking _too similar_ (e.g., 8 or 9 objects _looks_ almost the same). We thus are forced to slow down and start _counting_, which is prone to mistake. _**RIGHT**_: As a result of our experiental limitation of immediately perceiving quantity accurately, we need to _memorize_ the outcome of composing (combining) or decomposing large quantities, such as in the form of a _multiplication table_ (or _times table_).

:::

Of course, that is not all. We also learned that we can convince ourselves that the multiplication table is correct by just performing the calculation by ourselves, such as counting 5 times to five and adding all up.  

And here in lies the key: We can find out what the outcome of multipication is by _adding_:

$$
  5 + 5 + 5 + 5 + 5 = 25
$$

So, at least in this sense, we can think of multiplication almost as a "shorthand" for _repeated addition_:

$$
  5 + 5 + 5 + 5 + 5 = 5 * 5
$$

It's just "less to write", if you will.

[A minor point of potential confusion in the form of an ambiguity of sorts is the _notation_ that we learn with multiplication in that we use **_a_ * _b_**, **_a_ x _b_**, **_a_ · _b_**, and **_ab_** alike.]

Now, since multiplication is just repeated addition, we can rotate the numbers that are added (or multipled) around again without changing the result. Accordingly, the words we use to describe these numbers are one and the same again for the numbers that we multiply:

$$
  factor * factor = product
$$

Now, deeper thought about multiplication leads us elsewhere. There is actually something more interesting about what a (Cartesian) **product** is. It is a unique kind of combination, in fact. But for our current context, it is more helpful to grasp that there is a _link_ between addition (which many feel is relatively "easy" to do) and multiplication (which "feels" a bit more involved; partly because we quickly end up with much larger numbers).  

Now - what about **division**?  

$$
  25 : 5 = 5
$$

Well, we can think of it as the _inverse_ to multiplication, of course. In a sense, it is simply undoing what multiplication does:

% Multiplication
:::{div}
:class: hidden dark:block

:::{figure} ./images/multiplication_dark.png
:label: fig:multiplication
:width: 55%
Multiplication and Divsion are **inverse operations**. And both are just repeated Addition and Subtraction, respectively. Division as subtraction works by subtracting the _divisor_ until you reach zero (or a number less than the divisor), and count the steps of subtraction (i.e., the minus signs in the resukting equation). So, the correct formalism for _4_ : _2_ would be: _4_ **-** _2_ **-** _2_ = 0, with the result being _2_.

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/multiplication.png
:label: fig:multiplication
:width: 55%
Multiplication and Divsion are **inverse operations**. And both are just repeated Addition and Subtraction, respectively.  

Note that, technically, division as subtraction works by subtracting the _divisor_ until you reach zero (or a number less than the divisor), and count the steps of subtraction (i.e., the minus signs in the resukting equation). So, the correct formalism for _4_ : _2_ would be: _4_ **-** _2_ **-** _2_ = 0, with the result being _2_.

:::

And, once again we find: _While multiplication is commutative, its inverse (division) is not._  

This asymmetry, here too, may be why students often find division a bit more challenging than multiplication. But there is an added reason: Division is where often are first introduced to numbers that are not _natural numbers_.  

This happens when we learn about division that lead to fractions such as 7 / 3. The result has a "**remainder**, and we eventually learn that writing down the result in decimal points never ends. In other words, we encounter **infinity** for the first time. We also learn that we can get seemingly around that problem by **rounding** or **approximating** (e.g., 7:3 ≈ 2.33). None of that is trivial, and some of the feeling of confusion that we might have first experienced at this point of our math education might have started us to feel like we are "not good" at math from this very point on (and resurfaced when we encounter infinity again at later stages).  

[Not making things any less confusin, the _notation_ of division can be confusing in that we use **_a_ : _b_**, and **_a_ ÷ _b_**, and **_a_ / _b_**, and **$\frac{a}{b}$** alike.]

Still, we all probably feel like we do not feel confused by these four basic operations of arithmetic (addition, subtraction, multiplication, and division). So, so far the only interesting observation may be how they related via repetition (at least, this is usually not made as obvious when teaching these techniques).  

And since division is repeated subtraction, we need to be careful about the order of numbers that we divide. Our definition thus discriminates between these numbers (as was the case for subtraction):

$$
  dividend : divisor = quotient
$$

Or, perhaps more commonly:

$$
  \frac{\text{numerator}}{\text{denominator}} = \text{quotient}
$$

However, the final operations of arithmetic often _do_ cause high-schooled learners a bit of concern. And there is a good reason for that - they do not seem to fit as neatly in what we discussed so far.  

Specifically, **exponentiation** does _not_ have one inverse operation. It has _two_: the **logarithm**, and the **root**. This can seem arbitrary. However, nothing is arbitrary in mathematics. In fact, these operations fit perfectly inside our scheme, and the fact that there are two inverse operations then makes perfect sense.  

So, we just continue what we started: addition, repeated, becomes multiplication.  
Multiplication repeated becomes exponentiation.  

$$
  \text{base}^{\text{exponent}} = \text{power}
$$

Taking a _base_ number to an _exponent_ just means that we multiply the base number with _itself_ as many times as prescribed by the exponent.  

$$
  5^{3} = 5 \cdot 5 \cdot 5
$$

Why two inverses then? Well, exponentiation has two parts: the **base** and the **exponent**. So, we need two operations to find one or the other.  

**Root (with the exponent as index/degree) returns the base.**  

**Logarithm (to that base) returns the exponent.**  

[for natural-number exponents and positive bases.]

% Inversion
:::{div}
:class: hidden dark:block

:::{figure} ./images/inverse_dark.png
:label: fig:inversion
:width: 97%
Arithmetic operations and their inverse.

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/inverse.png
:label: fig:inversin
:width: 97%
Arithmetic operations and their inverse.

:::

The logarithm can also be thought of as repeated division (in that we are counting how many times you can divide by the base before reaching 1).  

This realization creates a _structure_ for arithmetic (in the broader sense that includes exponentiation, roots, and lograrithms) where each of these operations shares a relation to one or more of the other operations.

% Arithmetic
:::{div}
:class: hidden dark:block

:::{figure} ./images/arithmetic_dark.png
:label: fig:arithmetic
:width: 97%
How the pairwise operations of arithmetic relate.

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/arithmetic.png
:label: fig:arithmetic
:width: 97%
How the pairwise operations of arithmetic relate.

:::

And now we are almost done. As you will see in the next chapter, there is a good reason that we slowly built up to an understanding what a logarithm is by using simple addition as our starting point. Logarithms _rule_ much of our perception. So, it is good to know that all that really is - a logarithm of a number - boils down to an _exponent_, another number (that yet another number, the base, has to be raised by to produce the number that we started out with). It is just the inverse of exponentiation, which itself is just iterated multiplication (which is iterated addition) - if we limit ourselves to natural numbers.  

This can be a helpful realization since logarithms result in curved graphs (functions), which are a bit more challenging to intuit than simple lines. But is exactly this property that makes logarithms interesting and powerful.  

% Log
:::{div}
:class: hidden dark:block

:::{figure} ./images/log_dark.gif
:label: fig:log
:width: 40%
Logarithmic curve as inverse of an exponential function.[^4]

:::

:::{div}
:class: dark:hidden

:::{figure} ./images/log.gif
:label: fig:log
:width: 40%
Logarithmic curve as inverse of an exponential function.[^4]

:::

[^4]: [public domain source](https://commons.wikimedia.org/wiki/File:Function-log-animation.gif)

We already established that when it comes to mental _calculation_, and multiplication in particular, we tend to struggle with large numbers. Logarithms come in handy in that they transform the multiplication of two very large numbers into simple addition. That is, if we know the logarithms (to the same base) of two large numbers, we can calculate (the logarithm of) their product by just adding the two logarithms:  

$$
  \log(xy) = \log(x) + \log(y)
$$

[as long as _x_ and _y_ are positive and the base is a positive number other than 1.]

In practice, this means that if we have a long list, or table, of logarithms, we can quickly multiply two large numbers by converting them back-and-forth into their logarithms. You might find that unimpressive, but before we all had easy access to powerful electric calculators or computers, this technique was key for scientists and engineers alike. In fact, using this technique (applied to _slide rules_) was still common when **NASA** developed the rockets used for the **Apollo** moon landing program.  

As we will see in the next chapter, discoverig a role for logarithms in perception science thus was especially exciting for the scientists at that time.  
