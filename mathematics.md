# MATHEMATICS

Science rests on mathematics, so we cannot completely avoid the topic. The following is a brief refresher for the (very limited) mathematics that we will use later on this course. We will start by assuming zero knowledge about mathematics, and then built up quickly from there. If you feel, at any step, that we moved to quickly, this may signify that there is need to brush up a bit via self-study. A few, hopefully helpful, sources and references are provided to do just that.  

    No calculations required.

As we already discussed, due to our schooling, we tend to think of mathematics as calculating, or resolving equations. This can turn since into a competition of sorts, where there is a correct solution (that an "authority" such as a teacher or a textbook author) knows and we can either fail or succeed in finding out. We will do none of that. Instead, we will ponder a bit more about the fundamental assumptions and operations that _underly_ this process. The goal is still to read and understand mathematical formalism and descriptions, but with a focus on _meaning_ (the information contained within) rather than computing or deriving a correct outcome by ourselves. Hopefully, this will also allow you to see mathematics "in a new light", and add a bit of _fun_, or at least make it all seem a bit more _interesting_.  

## FOUNDATIONS

We already discussed that modern mathematics starts with one or more _axioms_ that one has to accept without further questioning. So, what are the axioms that underly _all_ of mathematics (or, since one can always drop or add axioms and thus change mathematics, the largest body of mathematics)?  

The currently most commonly considered axiomatic foundation of mathematics is **set theory**, specifically the _Zermelo–Fraenkel_ set theory with an additional axiom (the _Axiom of Choice_), abbreviated as **ZFC**.  

You might now wonder: "How many axioms will I need to accept as a foundation of mathematics?". In other words, what is the minimal number of axioms that we can reduce the theorems of a large body of mathematics to? What is the number of axioms that make up ZFC?  

The answer is (in the most common formulation): 9.  

No worries - we will not have to go over all of these axioms. Instead, we will just take note, ponder for a moment whether this number of axiom seems surprisingly high or low, and move on. What we really want to do is take a brief look at the most basic "picture" that set theory provides and use it to get a sense of what we mean by "number" (yes, we will keep it that simple). Then we will see what we can _do_ with numbers, resulting in basic **arithmetic** (addition, subtraction, multiplication, and division). After we discussed _exponentiation_ and _logarithms_, we will be largely done.  

You might feel that you understand all these things already, so why bother? In fact, we will assume that you already do. However, remember that we started out with _radical doubt_, and deriving some certainty from a combination of experience and logic. We also started out by striving for _coherentism_ in our knowledge in probing for the possibility of a unified whole of science. We thus need to explore whether mathematics, which might have been taught to us as an isolated fragment of knowledge fits in our _singular_ approach that we have started. In other words, you probably already know much more about numbers, addition, and even logarithms than we discuss here, but we will aim to look at them from a perspective, a new light perhaps, that unifies all them in some sense rather than a diverse set of lenses that we have to choose from and wear one-at-a-time.  

There is, fo course, a lot to say about ZFC. The Axiom of Choice, for example, is highly contentious. There is also an alternative proposal for a foundation of mathematics called **category theory**. We will consider the difference between these two starting points of mathematics in a bit since it might be relevant for how we approach mathematics in the context of perception. But for now, let us stick to set theory since - as you will see - it can help us to somewhat intuitovely derive the basic mathematics we require.  

## NUMBERS

    Ask three mathematicians what a number is. 
    You’ll get five definitions.
    And all of them will be correct.

Now that we have gained a (very) basic understanding of set theory, which we identfied as the foundational basis of much of mathematics, we can explore the concept of numbers. "Why just now?", you might wonder. After all, (pre-)school mathematics tends to start with numbers, and builds from there, often teaching set theory at a much later stage.  

However, we needed to start from _foundations_, and numbers are commonly derived by modern mathematics using the axioms of set theory (ZFC). More so, since we already are at a point where we ponder things more deeply, numbers are not as simple as they look at first sight. Thinking about numbers (deeply) can quickly turn puzzling. And having set theory as a backdrop can help prevent a bit of that.  

## ARITHMETIC

Now things get really interesting. Numbers by themselves just seem to "exist" and "not do anything". And when we were young, we probably quickly realized that numbers really show their usefulness once we add, subtract, multiply, or divide them.  

And all of that seems to come quite naturally. After all, we can do the same thing with concrete objects: add one apple to two others, divide a pizza in half, and so on.  

But things can become a bit confusing, or non-intuitive rather quickly:

**Addition** allows us to disregard order: 2 + 4 is the same as 4 + 2. Both is 6.  

    4 + 2 = 2 + 4

The fancy word for this property of addition is **commutativity**.

**Subtraction** seems to be a simple inverse process. We just reverse what we just did.  

Let's say we added 2 apples to 4 apples:

    2 + 4 = 6

We can just take these 2 apples away again. Undo addition - and get subtraction:  

    6 - 2 = 4

But if this subtraction is basically the same as addition, just the other way around, a kid who discovers all might be surprised that there is a big difference: Subtraction is not commutative.

    6 - 4 = 2

Indeed, many people feel that addition is a bit more "easy" than subtraction. And the fact that additivity is a bit more "lax" in that you disregard order while subtraction requires you to make sure that you do not accidentally confuse the order might be part of that reason.  

For now, all we should do is put an earmark in this very simple observation. Arithemtic seems easy since we can think of subtraction as the inverse of addition. And yet, there is an added bit of complexity in that these two operations are not quite as fully _symmetric_ as it seems. Different rules apply for each.  

Now let us move on to **multiplication**.  
