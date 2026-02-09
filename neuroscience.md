# NEUROSCIENCE

% BASIC BRAIN
:::{div}
:class: hidden dark:block

:::{figure} ./images/basic_brain_dark.png
:label: fig:basic_brain
:width: 60%
Mid-line section of a human brain.[^1]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/basic_brain.png
:label: fig:basic_brain
:width: 60%
Mid-line section of a human brain.[^1]
:::

[^1]: [public domain source](https://commons.wikimedia.org/wiki/File:Gray720.png)

Before we examine each of our senses in isolation, we first need to briefly review the common denominator - the basic physiological function of the brain. The goal is to introduce anyone to the foundations of how neuroscientists currently think about brain function. The focus will be on **neurophysiology**, which is mostly interested in the biological and biochechemical action that underlies brain activity. That is, we will review neuronal _communication_, or _interaction_.  

Neuronal **activation** is only half of the story when it comes to understanding the link between sensation, perception and the brain. We will also need to briefly examine neuronal **connectivity**. After all, if we isolate each neuron of interest in a dish, and observe the same patterns of neuronal activation for each of these isolated neurons, we would not expect perception to arise. It is only because neurons form a _causal network_ that the brain does more than host individual, isolated ON/OFF switches.  

If you already have basic training in systems neuroscience, you can probably skip this chapter since we will merely go over the very basics of neuronal function and neuroanatomy. However, you might want to browse through this page to ensure that we are not covering anything that you might want a quick refresher for. You might also want to check out the end of this chapter, where we briefly discuss the difference between the _computational_ metaphor of brain function and _information processing_ since this distinction is not usually taught, or made explicit, in neuroscience courses.  

## NEURONAL ACTIVITY

Alcohol and other drugs can strongly alter our perception. Few people dispute that these chemicals do so by altering the chemistry of our brain. In the same vein, certain brain disorders and lesions that alter perception, such as losing the ability to see color or motion (we will discuss these clinical cases in detail at a later stage of the book) lead us to the same conclusion. If we undergo a major surgery, we find relief in the fact that an anesthesiologist will use chemicals in an attempt to alleviate us from consciously experiencing the associated pain. The same goes for dentists using chemicals locally to disrupt nervous function. Even a simple cold that robs us of our sense of smell seems clearly linked to the physiology of the nose and its link to the rest of our nervous system. The link between the brain and perception thus seems obvious.  

Once someone interested in perception appreciates the link between brain mechanisms and conscious experience, their focus tends to shift to _neuronal activation_. Not surprisingly, then, most of systems neuroscience (the subfield of neuroscience that studies brain function), has focused on **measuring brain activation**.  

There are many ways to study brain activity. Most of them have one assumption in common: they are fundamentally interested in the activation of sets of _single neurons_ (in the form of action potentials). That is, even techniques that do not measure single neurons directly, resort to _mechanistically_ explain their measures as _collective action_ (**mass action**) of large sets of individually activated neurons. We thus will first (superficially) review what is known about single neuron activation, followed by a brief discussion of some of the most common techniques and measures that systems neuroscientists, psychologists, and cognitive scientists use to record neuronal activation.  

### Neurons

% NEURON
:::{div}
:class: hidden dark:block

:::{figure} ./images/neuron_dark.png
:label: fig:neuron
:width: 20%
Sketch of a single brain cell (neuron). Neurons are generally divided into three sections: **Dendrites** are extensions where most (but not all) inputs of other neurons are received via **synapses**. Dendrites extend to the main cell body, or **soma**, where the main output of neurons (**action potentials**) originate. Action potentials travel down extensions called **axons**, which can extend across many centimeters or more. At the end point of axons, neurons tend to form synapses that innervate other neurons.[^2]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/neuron.png
:label: fig:neuron
:width: 20%
Sketch of a single brain cell (neuron). Neurons are generally divided into three sections: **Dendrites** are extensions where most (but not all) inputs of other neurons are received via **synapses**. Dendrites extend to the main cell body, or **soma**, where the main output of neurons (**action potentials**) originate. Action potentials travel down extensions called **axons**, which can extend across many centimeters or more. At the end point of axons, neurons tend to form synapses that innervate other neurons.[^2]
:::

[^2]: [public domain source](https://commons.wikimedia.org/wiki/File:Gray627.png)

Neurons come in many shapes and sizes, even within the same part of the brain. However, we can identify the main parts of neurons across almost all of these cell types.

% Neuronal Parts
:::{div}
:class: hidden dark:block

:::{figure} ./images/neuron_parts_dark.png
:label: fig:neuronal_parts
:width: 60%
The main parts of a neuron.[^3]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/neuron_parts.png
:label: fig:neuronal_parts
:width: 60%
The main parts of a neuron.[^3]
:::

[^3]: [public domain source](https://commons.wikimedia.org/wiki/File:Dendrites_(PSF).png)

### Action Potentials

% Neuron Signals
:::{div}
:class: hidden dark:block

:::{figure} ./images/neuron_signals_dark.png
:label: fig:neuronal_signals
:width: 30%
The flow of electric signals across neurons is from **synapses** at the **dendrites** (where most signals from other neurons arrive) to the **soma** (cell body) to **axons** until they terminate in **synapses** that connect to other neurons.[^4]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/neuron_signals.png
:label: fig:neuronal_signals
:width: 30%
The flow of electric signals across neurons is from **synapses** at the **dendrites** (where most signals from other neurons arrive) to the **soma** (cell body) to **axons** until they terminate in **synapses** that connect to other neurons.[^4]
:::

[^4]: [public domain source](https://commons.wikimedia.org/wiki/File:ANN_neuron.svg)

% Action Potentials
:::{div}
:class: hidden dark:block

:::{figure} ./images/action_potential_dark.png
:label: fig:action_potential
:width: 55%
Diagram of an action potential. Action potentials are brief (~1ms) all-or-none impulses. That means they either occur or do not occur. And if they occur, they always more or less take on the same shape (they "look the same" on an oscilloscope). However, they are not just brief blips. Instead of a singular, brief, vertical line, they take on a somewhat more complex curved shape that contains several distinct periods of time. These main periods are: **depolarisation**: The brief period where the neuron changes in the _polarity_ of its charge (i.e., neurons go from being negatively charged at rest to briefly having positive charge). **repolarization**: Following this brief rise in positive charge, the neuron returns to its usual negative charge (the _resting potential_). Interestingly, however, there is a brief period where this process "overshoots" and the neuron goes (even) more negative in charge than during rest. This period, where the neuron goes too negative and then returns to the _resting potential_ is called **hyperpolarization**. Another term used for the time period of hyperpolarization is the **refractory period**, which indicates that the neuron cannot get excited again during this time. Only once the refractory period is over, can a neuron start another action potential (i.e., fire another spike).[^5]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/action_potential.png
:label: fig:action_potential
:width: 55%
Diagram of an action potential. Action potentials are brief (~1ms) all-or-none impulses. That means they either occur or do not occur. And if they occur, they always more or less take on the same shape (they "look the same" on an oscilloscope). However, they are not just brief blips. Instead of a singular, brief, vertical line, they take on a somewhat more complex curved shape that contains several distinct periods of time. These main periods are: **depolarisation**: The brief period where the neuron changes in the _polarity_ of its charge (i.e., neurons go from being negatively charged at rest to briefly having positive charge). **repolarization**: Following this brief rise in positive charge, the neuron returns to its usual negative charge (the _resting potential_). Interestingly, however, there is a brief period where this process "overshoots" and the neuron goes (even) more negative in charge than during rest. This period, where the neuron goes too negative and then returns to the _resting potential_ is called **hyperpolarization**. Another term used for the time period of hyperpolarization is the **refractory period**, which indicates that the neuron cannot get excited again during this time. Only once the refractory period is over, can a neuron start another action potential (i.e., fire another spike).[^5]
:::

[^5]: [public domain source](https://commons.wikimedia.org/wiki/File:Action_potential_schematic.svg)

### Synapses

Synapses are the spaces between neurons where the parts of neurons that deliver signals (the **axons** of **presynaptic neurons**) come close to the parts of neurons that receive these signals (the **dendrites of postsynaptic neurons**). In between these neurons, there is a tiny gap - the synaptic cleft.

Does a gap imply that the electric signal (the **action potential**) that traveled down a neuron towards its axon (and ultimately, the **axon terminals**) comes to a stop? Yes. The electric impulse ends right there. It does not cross, or "jump" to other neurons - not directly. Just as would be the case for electric wires, the spatial gap electrically insulates neighboring neurons to a great degree.

However, the signal that the impulse represented does not stop at this point. What happens is more interesting: The electric impulse (the action potential) of the _presynaptic neuron_ gets converted to a **chemical signal** (in the form of **neurotransmitters**). That chemical signal crosses the synapse, and, depending on the circumstances, the _postsynaptic neuron_ might translate this chemical signal back into an electrical signal (a _postsynaptic_ action potential).

This way, neurons can do more than just pass on signals - synapses allow neurons to either pass on _presynaptic action potentials_ once they sense them as chemical signals at their dendrites, or not (in practice, what decides whether a _postsynaptic action potential_ is produced is simply **how many** chemical signals that neuron received in a certain amount of time).

The fact that signals - information - moves across our brains in _both_ electrical (action potentials) and chemical (neurontransmitters) form also explains why our brains can be changed in their activity either via electric means (as is done in certain patients that have electrodes implanted in their brain) or via chemical means (such as is done when we undergo general anesthesia for surgical procedures).

### Neurophysiology

% Neuron Signals
:::{div}
:class: hidden dark:block

:::{figure} ./images/spike_sequence_dark.png
:label: fig:spike_sequence
:width: 55%
A sequence of spikes in response to constant stimulation (a "spike train").[^6]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/spike_sequence.png
:label: fig:spike_sequence
:width: 55%
A sequence of spikes in response to constant stimulation (a "spike train").[^6]
:::

[^6]: [public domain source](https://commons.wikimedia.org/wiki/File:CBRD_for_Wiki.png)

### EEG / MEG

### fMRI

## NEURONAL CONNECTIVITY

% Reflex
:::{div}
:class: hidden dark:block

:::{figure} ./images/reflex_dark.png
:label: fig:reflex
:width: 50%
A reflex loop.[^7]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/reflex.png
:label: fig:reflex
:width: 50%
A reflex loop.[^7]
:::

[^7]: [public domain source](https://commons.wikimedia.org/wiki/File:Afferent_(PSF).png)

% James
:::{div}
:class: hidden dark:block

:::{figure} ./images/James_dark.png
:label: fig:James
:width: 55%
The **sensory-motor loop** that starts with sensing a physical stimulus, followed by the associated sensory-evoked neuronal excitation spreading across the brain from sensory to cognitive and motor areas, ending in motor areas activating muscles in our bodies, can be thought of as a very large and complex reflex loop.[^8]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/James.png
:label: fig:James
:width: 55%
The **sensory-motor loop** that starts with sensing a physical stimulus, followed by the associated sensory-evoked neuronal excitation spreading across the brain from sensory to cognitive and motor areas, ending in motor areas activating muscles in our bodies, can be thought of as a very large and complex reflex loop.[^8]
:::

[^8]: [public domain source](https://commons.wikimedia.org/wiki/File:Principles_of_Psychology_(James)_v1_p25b.png)

Now that we discussed neuronal activation, let us take a moment and ponder whether the study of neuronal activation (which seems _necessary_ for perception) is _sufficient_ to uncover the link to perception. The reason to do so is that the massive focus on activation risks forgetfulness about other contributing factors.  

Imagine that we find all neurons in our brain that correlate in a certain type of activity with the smell of banana. Now imagine that in the future it will be possible to create perfect copies - molecularly identical clones - of these neurons and let them grow as a cell culture on a Petri dish. The only difference between these clones and the neurons in your brain are their connections: while the neurons in your brain are connected via axons and dendrites, the neurons in the cell culture are all isolated.  

Now imagine that we are able to electrically stimulate the neurons in the cell culture in the exact same sequence as the connected neurons in your brain when you smell banana. Would you expect the unconnected neurons in the cell culture to collectively experience the same smell?  

This thought experiment evokes the notion that, no, activity _alone_ does not seem to be sufficient for a unified experience of the smell of banana. Their connectivity and signal exchange seems equally, or perhaps more, relevant.  

This conclusion leads us to an appreciation of **neuroanatomy** - the study of neuronal connectivity (and, on a deeper level, the question of what exactly signal exchange between neurons _does_ which seems to _add_ to neurons getting activated in a certain sequence). Let us do so next.  

### Neuroanatomy

#### Nervous System

#### Sensory Epithelia

#### Brain

> Brain, noun.  
> An apparatus with which we think that we think.
>
> -- A. Bierce (1911): 'The Devil's Dictionary'

#### Thalamus

#### Cerebral Cortex

% LOBES
:::{div}
:class: hidden dark:block

:::{figure} ./images/lobes_dark.png
:label: fig:lobes
:width: 60%
The four main lobes of the cerebral cortex.[^9]
:::

:::{div}
:class: dark:hidden

:::{figure} ./images/lobes.png
:label: fig:lobes
:width: 60%
The four main lobes of the human cerebral cortex.[^9]
:::

[^9]: [public domain source](https://commons.wikimedia.org/wiki/File:Gray728.png)

## NEURONAL INTERACTIONS

Now that we have discussed the combined role of neuronal activation and neuronal connections, we need to face a final open question: _how do these two factors combine_? That is, we established that both neuronal activation and neuronal connectivity seem to matter. This seems trivial, in a sense, in that their combined effect is some sort of **neuronal interaction**, or signal exchange. On a deeper level, this leaves us with another mystery, however: _how does signal exchange support perception_? What is it about signals traveling along chains of neurons that this process comes with us, say, smelling the scent of banana? There are several views and suggestions in the literature. And much of that is at the leading edge of research, with new insights and ideas arriving in steady fashion.  

However, we can distill two perhaps overlapping, or perhaps contrasting, views that are increasingly dominating the literature:  

The first view is that neuronal interactions are **computations**. This view raises the question of what that is exactly - a computation (and if and how neuronal computations relate to what a computer does). What follows from this view that our search for a link between brain mechanisms and perception should be guided by looking for _computational mechanisms_ that support perception.  

The second view is that neuronal interactions are a form of **information exchange**, or **information processing**. This view can be reconciled with seeing computations as fundamental in that one can interpret as information processing as well. However, one can also interpret information processing as a broader term that goes beyond the classic definition of computation (to which a computationalist might reply with a broader definition of computation). One of the most common views of a separability between computations and information processing is the view that the brain performs **information integration**, and that it is this process that supports perception - with the main difference between the two is that computations focus on change (state **transitions**) while information integrations focuses on static **states** (the start and endpoint of transitions). This view raises additional questions surrounding what we mean by "information" as well as by "integration". Let us unpack all that.  

### Computations

We tend to take the term "computation" for granted and well-defined. In a simple sense, it seems to refer to what a computer does. There is a close similarity to the concept of "calculation", except we understand that computers operate on 0's and 1's only. Indeed, one can describe much of what modern computers do as **Boolean Logic**.  

In our section on _Logic_, we already discussed that classical logic only allows for two states: _false_ and _true_. Boolean logic simply uses 0 for _false_ and 1 for _true_. As a result, Boolean Logic is a **binary logic** that only allows for two values.  

You might remember that there are also **multi-valued logics**, such as intuitionist logic, which allows for a value "in-between" true and false (such as "undecided"). If we base brain function on Boolean Logic exclusively (as our modern computers do), we might miss something important in case the brain (neurons) operate on multi-valued logic. This is worth keeping in mind. However, remember that human brain cells seemingly use _all-or-none_ activation in terms of action potentials, so it does not seem unreasonable that the exchange of action potentials gives rise to a Boolean Logic in the brain. More so, the rise of AI and LMM's in particular seems to suggest that we can get machines to mimic human cognitive function to some degree using the same basic principle of Boolean Logic (realized _in silico_ rather than _in vivo_). So, for now let us assume this to be the case. We will revisit this assumption at a later stage.  

The next step to understand Boolean is to incorporate what we learned about _set theory_. There is an interesting parallel between the _operations_ of Boolean Logic (i.e., what happens to the 0's and 1's in a Boolean Logic Circuit) and the mathematical principles of set theory.  

It is important to note that so far our discussion on computations was somewhat myopically focused on what a _particular type_ of computer performs. Indeed, the original definition of "computation" was broader, and somewhat more abstract. The term "computation" was coined by A. Turing, and he defined it as:

    a number is computable if its decimal can be written down by a machine

This definition raises a lot of questions about what exactly defines "a machine", and Turing answers all of that by defining a very specific machine (the **Turing machine**) that fulfills this definition.  

### Information Integration

The rise of {abbr}`LMMs (Large Language Models, such as ChatPGT)` has given many people pause as to the assumption that classical computations, as discussed above, support perception. While {abbr}`LMMs (Large Language Models, such as ChatPGT)` compel us to admit that much of their written output resembles that of thinking humans, there is lingering debate (and in fact, much doubt) about whether LMM's perceive _anything_ in the process.  
