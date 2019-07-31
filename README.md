# CSKey
The perfect keyboard layout for all computer scientists. It supports a wide selection of Greek letters and mathematical symbols. The entire layout was designed to feel natural. If a natural placement of the symbol was not possible, I at least made sure there is an easy mnemonic.

## Layers
There are the usual two layers for the usual roman letters in qwerty format, lowercase without any modifiers and uppercase with the shift modifier.

### Option (⌥) Layer
The option and shift-option layer provide access to Greek letters. Once again, the shift button switches from lowercase to uppercase.

There are two flavors of the layout available: with or without German Umlauts. I'll first explain the rationale behind the layout without the Umlauts and then point out the differences when opting for Umlauts.

Generally, when there is a one-to-one correspondence between Roman and Greek letters, the keyboard layout will reflect it. The epsilon (ε), for example, corresponds to the letter e. This becomes evident when checking out the upper case variants. Greek: E, Roman: E. You see the difference? If so, you should get your eyes checked, man...

The uppercase variant of the letters is always a decent indicator even if the lowercase variant is not so clear, consider e.g. ρ/R. This covers most of the letters. There are a few exceptions, though.

The letter psi (ψ/Ψ) has to obvious Roman counterpart. It does, however, look somewhat like a y with an extra prong, which is why you'll find it exactly there. 
Phi (φ/Φ) does not look like an f, it does sound like it though. Also, in a mathematical context, it's often used as the Greek counterpart of f, so this is where it lives on the keyboard. 
Then there is omega (ω/Ω) where both o and w are decent choices. And since neither was occupied, yet, ω is accessible from both keys. 
So, the last remaining problematic case is theta (θ/Θ). And, boy, this letter is annoying. I'd put it on the t because theta starts with this letter, but tau (τ/T) is a better candidate for the key. The perfect place would be the thorn (Þ/þ) key, but _someone_ decided to get rid of this letter. Thank you very much...
Long story short: theta is on the j key. No mnemonic, no clever connection. Sorry.

Let's sum up the less obvious choices as a cheat sheet:

| Greek Letter | Key         | Mnemonic                         |
| ------------ | ----------- | -------------------------------- |
| ψ/Ψ          | y/Y         | ψ is y with an extra prong       |
| φ/Φ          | f/F         | Phi sounds like f                |
| ω/Ω          | w/W and o/O | ω looks like w and sounds like o |
| θ/Θ          | j/J         | θ is a di**                      |

#### German Umlauts
So if you're one of us Germans and sometimes need to throw a couple of üs and äs into the mix, I got you covered. During setup, I'll ask whether you need Umlauts, if you type something starting with `y`, I'll install a slightly modified option layer for you.

You can find ä on the a key, ü on the u key, ö on the o key, and --- I know, it's technically not an Umlaut --- ß on the s key. Fun fact: there is even the uppercase ẞ available, even though barely anyone knows about its existence (because it's pointless most of the time).

So, let's discuss conflicts. The ö evicts good ol' omega (ω/Ω). That's not too bad, so you just need to fall back on the w key. Phew. The ü evicts nothing at all --- even better! The ß kicked σ off its place, it now lives on the q key. That's easy to remember because σ is just a slightly misshaped q that was rotated counter-clockwise by a couple of degrees. Lastly, the α gave me a bit of a head ache. I opted for putting it on the v key because a capital A somewhat looks like a V rotated by 180 degrees. Not perfect, but the best I could come up with. That's what you get for typing German!

Let's sum up the less obvious choices again:

| Greek Letter/Umlaut | Key         | Mnemonic                         |
| ------------------- | ----------- | -------------------------------- |
| ψ/Ψ                 | y/Y         | ψ is y with an extra prong       |
| φ/Φ                 | f/F         | Phi sounds like f                |
| ω/Ω                 | w/W         | ω looks like w                   |
| θ/Θ                 | j/J         | θ is a di**                      |
| σ/Σ                 | q/Q         | σ is a rotated, misshapen q      |
| α/A                 | v/V         | A is a rotated V missing its bar |

### Math Mode
So far we just combined two character sets --- nothing to write home about.
Let's add math to the mix, shall we?

For this, we will enter the math mode of the keyboard layout. Strictly speaking, the math mode is a a dead accented character. When you press option+shift+m (which is the same as option+M), the next character will receive special treatment. This will only affect the next character, so to write a sequence of letters you will always need to press option+M before each letter anew. While this put me off initially, this never turned out to be annoying. Even when you want to typeset a formula such as `∀φ ∈ P: ◻φ → (◇¬α ∨ ◻β)`, you will spend the most time being glad that not every character has to be spelled out entirely and preceded by a backslash `\forall\phi\in P\colon \LTLbox\phi \implies (\LTLdiamond\neg\alpha \lor \LTLbox\beta)`. Trust me on this: it's not a big deal, you'll see.

Now, I won't go over every letter by itself. There are some noteworthy patterns in the key assignment I want to point out, other than that there will be a nifty table at the end.

First note that there is two math layers again: the regular and the option layer, all of them have a shifted/uppercase variant. That means there is a total of four math layers. That's pretty overwhelming at first and needs _some_ getting-used-to. However, try to nail your most frequently used symbols first, after a while you'll start to demand more pretty symbols and learn the next batch until you master the entire board and become a unicode god. Or godess. Sigh, who am I kidding, there are no women in computer science. Nor on the entire internet. At least, that's what I heard.

In general, if there is an obvious counterpart to a mathematical symbol, chances are you will find it on this very key. Examples: ∀ is on the math mode a, ∃ is on the math mode e, ◻ (*g*lobally) is on the math mode g. I'll refrain from referring to them as "math mode something" from now on. Same goes for symbols: the logical conjunction ∧, a.k.a. "and", is on the ampersand (&), disjunction ∨ on the pipe symbol (with an without shift for maximum convenience), Cartesian product × on the asterisk *, power of two/three ²/³ on 2/3. 

The comma and period become three dots … and ⋯. The former greater > and less < symbols become greater-equal ≥ and less-equal ≤ and so on and so forth.

Whenever applicable, shift *negates* symbols. So math mode e is ∃, math mode E is ∄.

Since I'm starting to grow bored listing off these symbols, here is the table:
The mnemonics are incomplete, sometimes there is none but I found the symbol useful anyway, sometimes the connection was too obvious, sometimes I was too lazy to write up a mnemonic. I might add them later.

| Math Symbol | Key | Mnemonic |
| ----------- | --- | -------- |
| ¬   | 1   | 1 features ! which is used for negation |
| ²/³ | 2/3 | |
| ∧/∨ | &/\| | |
| ×   | *   | Arithmetic v. Cartesian product |
| ×   | c   | **c**ross product |
| → | - | Just add the hook at the end |
| ↛ | _ | Shift version for negation (doesn't work in all fonts) |
| ≈ | = | |
| ≠ | + | Shifted version for negation |
| ℚ | q | |
| ℝ | r | |
| ℤ | z | |
| ℕ | n | |
| ∃/∀ | e/a | |
| ⊤ | t | true/top |
| ⊥ | b | bot/bottom | 
| ~ | s | `\sim` in LaTeX |
| ◻/◇ | g/f | **g**lobally, **f**inally | 
| ⌊/⌋/⌈/⌉ | [/]/{/} | Slightly mutilated square bracket |
| ∫ | / | Kinds looks like it? |
| ↯ | ` | I got nothing... |
| ⊆/⊇ | ;/' | | 
| ⊈/⊉ | :/" | Shifted version for negation |
| ∈ | i | `\in` in LaTeX |
| ∉ | I | Shifted version for negation |
| ⊕ | x | |
| …/⋯ | ,/. | |
| ∪/⋂ | u/option+u | |
| ← | option+- | Turn around → |
| ⟷ | option+= | |
| ⇎ | option++ | negation of ⟷ |

## Attribution
The layout was created using [Ukelele](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele), which looks like a spelling error but turns out to be an awesome utility to create custom keyboard layouts. Keep up the great work, folks!

# About me
I'm a PhD student at Saarland University. Saarland is a part of Germany (at least most of the time), which explains why I took Umlauts into account. I have a fable for typography and other shit no sane person cares about. This does not restrain me from tormenting my students with the thousand ways of typesetting an "f" in LaTeX such that the kerning works out. So, naturally, I love unicode for more than its Emojis and want to use it EVERYWHEREEEE. Away with the days where you write un-rendered LaTeX code in Emails, there future is now, old man!

However, none of my friends actually care particularly about the unicode capabilities of their keyboard. This was mind-numbingly disappointing, so I decided to bore even more people using the all-mighty internet. Now, people can not-care about this matter all over the globe. What a time to be alive!

In all seriousness, I think using unicode symbols rather than inline LaTeX macros in text makes parsing it so much easier. This is why I want to offer a convenient solution applicable to everyone out there. Feel free to use and share the layout! Happy typing!
