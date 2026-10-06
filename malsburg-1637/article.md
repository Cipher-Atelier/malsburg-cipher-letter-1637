# A Five-Letter Key in a 1637 Cipher

How correcting a manuscript transcription made a ten-line cipher readable, and what an AI-assisted decipherment still needs to prove.

Author: Maxim Egorov

Prepared (source preparedUtc): 2026-10-02T13:26:06Z

Source: [published article](https://maxim-egorov.dev/research/malsburg-1637/). Exported from the already-published article on 5 October 2026. The preparation timestamp is preserved as supplied; it is not a new publication date. Article wording is preserved below; site-specific HTML presentation has been converted to Markdown and site-root links have been expanded to absolute website URLs.

[Investigation index](README.md) · [Methods](methods.md) · [Readings](readings.md) · [Sources](sources.md)

A historical cipher looks like a cryptography problem. Sometimes the first problem is the input.

At the foot of a letter dated January 1637 sits a separate block of ten lines in lower-case letters. Our AI-assisted analysis gives a continuous German reading using a period-five scheme equivalent to Vigenère. The useful part of the story is how we got there: overlapping pen strokes had introduced letters into the transcription that were never separate letters on the page.

The result covers all 510 retained, normalized letters. It does not identify every person in the message, recover cancelled writing, or close the surrounding correspondence. Three conspicuous defects remain in the reading. This is a reproducible decipherment proposal awaiting external verification.

The result was verified internally on **2 October 2026 at 13:06 UTC**. The publication time is recorded separately above; external verification remains pending.

## What the block says

The passage concerns a possible departure, disagreement with Swedish generals over command, the need to join forces and a request for absolute authority. Its grammar leaves an important question open: it may recommend what [LL] should write, rather than report a decision already made.

Here is a revised English interpretation. It treats the opening as conditional and retains the possible proposed-letter scope. “Troops” and “present” interpret the difficult forms `tqouppen` and `itzigdn`; the literal German below is unchanged.

> [43] is now on the point of making a move, perhaps leaving. If [45] wish to be rid of him and can do without him, now is the time for [LL] to write, perhaps to this effect: they see that he would not agree with the Swedish generals over command; the situation of [45] required their [troops] to join the Swedes, and the Swedes to join them; the actions of [LL] no longer pleased him; and they could not grant the absolute authority he sought. They would leave him to decide what he wished to do, would not detain him against his circumstances, and would have him satisfied according to their [present] situation and means.

This is one grammatical interpretation, informed by the later critical reading linked above. That edition uses a different source reading at this point, yielding `soistes` rather than our preserved `seistes`; its reading is not a new output of the ciphertext published here. The transition around `seistesnunzeitdas[LL]schreiben` remains difficult; a recommendation followed by reported circumstances is another possibility. Neither reading establishes an actual dismissal, completed troop movement or a settlement already agreed. The German’s singular `er` with plural `wurden` also remains unresolved.

“Estat” may describe circumstances, resources or position. “Contentiren” means to satisfy; payment or settlement is possible but not established. The values and referents of [43], [45] and [LL] remain unknown. [LL] is a provisional label for angular signs.



## Correction and source update · 5 October 2026

The [original 2 October article (archived text)](https://maxim-egorov.dev/downloads/research-archive/malsburg-1637-before-2026-10-05.txt) described the source report as leaving this block unread. That statement referred to the September report; the source has since changed. The credit below now distinguishes the dated versions. This revision also replaces the unverified folio label with the digital-image number and corrects the English interpretation: the opening may be conditional and the later clauses may describe a proposed letter, rather than decisions already taken. The previous Russian rendering is retained in the linked original article, not repeated here. The literal German, cipher input, code and downloadable research package are unchanged.



## Source and earlier work

This work starts with Daniel Bourdeau’s [report at the 29 September 2026 UTC revision](https://github.com/dbourdeau/cyphersolver/blob/ceb348247471669ddf83f4c9061266d660d22879/docs/malsburg1637.html) and [the research materials at that revision](https://github.com/dbourdeau/cyphersolver/tree/ceb348247471669ddf83f4c9061266d660d22879/targets/malsburg1637). He largely deciphered the numerical correspondence and supplied the transcription and research context that made this investigation possible. That version left the separate alphabetic block unread. The block is the scope of our result.

The [current report](https://dbourdeau.github.io/cyphersolver/malsburg1637.html) and [current materials](https://github.com/dbourdeau/cyphersolver/tree/main/targets/malsburg1637) now include a contribution credited to Larry Beck with ChatGPT, with the same repeating shifts and a critical reading. Its [recorded commit](https://github.com/dbourdeau/cyphersolver/commit/51fb42c3b4adf5e8eb8823cfed63c9cc8ac80afe) is dated **2 October 2026 at 23:51:09 UTC**; this article was published at **14:13:26 UTC** that day. These timestamps document the visible publication sequence. They do not establish discovery priority, dependence, copying or endorsement.

The manuscript is held by **Hessisches Staatsarchiv Marburg**, shelfmark **HStAM 4 h Nr. 1411, digital image 0012**, available through [HCPortal record 497](https://crypto.hcportal.eu/dashboard/cryptograms/497). The earlier label “f. 12” followed the source report; manuscript foliation has not been verified. The portal dates the item 17 January 1637 and lists its sender and recipient as Unknown. Bourdeau attributes the enclosing letter to Otto von der Malsburg, writing from Wesel on 7/17 January to Landgrave Wilhelm V and the Hessian court. That attribution does not establish who wrote the separate block.

Bourdeau releases his report text under CC BY 4.0. The archival scan has separate provenance; this article links to the [source image](https://api.hcportal.eu/media/1395/79511677516420.jpg) rather than assuming that the report’s text licence covers the image.

## The transcription changed the problem

The research used Chappie, my AI assistant, for image analysis, code, candidate testing and review. AI agents carried out the glyph comparisons and computational checks recorded in the research package. I am documenting that assisted workflow here; I did not personally transcribe every manuscript character or perform the paleographic audit by hand.

The first image-based audit compared the transcription with the scan before using a proposed plaintext or key. A second image-based review assessed the proposed edits against the pixels and the surrounding rows. These were separate reviews within the AI-assisted workflow, not outside expert peer review. The existing transcription was available to them, so the audit was not a blind transcription.

The most consequential errors came from the distance between rows. A long descender belonging to a letter above could look like an extra upright `l` in the line below. Following the stroke back to its origin removed fifteen such false letters. Another apparent marked `u` was two separate dotted uprights, `ii`. The review also distinguished straight-tailed `q` shapes from looped `g` shapes and restored an omitted terminal letter.

Of 36 proposed edits, 34 were supported, one was rejected, and one bare/marked-`u` distinction remained unresolved. The rejected change stayed rejected. The unresolved reading stayed in the variant set. The resulting count was a consequence of the visual reading, not a target the reviewers were asked to reach.

This matters for a repeating-key cipher. Insert one false character and every following letter takes the wrong key position until another error happens to compensate. A more elaborate solver cannot repair that alignment reliably if the input has already been treated as certain.

## One alphabet, one key, one continuous stream

The successful scheme is equivalent to ordinary Vigenère over this 24-letter alphabet:

```text
abcdefghiklmnopqrstuwxyz
```

It folds the historical `i/j` and `u/v` pairs. The transcription labels `ü` and `ÿ` are normalized to `u` and `y`. Those labels describe manuscript shapes; this normalization does not prove the meaning of the writer’s marks.

Our representation of the encryption key is **EFDGC**, or zero-based shifts **4, 5, 3, 6, 2**. This does not establish that the historical writer used those letters as a keyword. To decrypt, subtract the next shift modulo 24. Continue the key across manuscript line breaks.

The numbers **43** and **45**, and the angular pair recorded as **LL**, remain visible in the diplomatic text but do not consume key positions in this model. The cancelled patch contributes zero retained positions. That is a counting rule for the surviving stream, not a recovery of what was overwritten.

The beginning is easy to inspect: `h k ü` normalizes to `h k u` and decrypts to `d e r`. After the following [43], the next letter uses the fourth shift. The key does not restart.



## Checks and limitations

A period-five structure emerged in the revised stream. The analysis retained explicit alternatives for uncertain glyphs, marker treatment and segmentation rather than accepting one convenient count without comparison. The signal survives the reviewed bare/marked-`u` alternatives and selected patch-count stress tests when markers are omitted. It does not survive every convention that consumes the markers as cipher positions.

The key was fitted with historical-German letter frequencies using the first 350 letters. The final 160 were excluded from that key fit and still produce a sustained German continuation. They had already participated in period discovery and transcription review, however. This is not a pristine holdout experiment.

A separately written decoder and forward encoder reproduce all 510 normalized positions with zero mismatches. That establishes that the published transformation and alignment are internally consistent. It cannot prove a key on its own: any invertible transformation can reverse its own output.

The stronger case is the combination: one simple key works throughout, the full output has sustained German syntax and a coherent subject, the reading has an inspectable archival source, and the declared alternatives and independent implementation checks expose where it is stable and where it is not. These checks support a reading. They do not certify unique paleography or the identities hidden in the markers.

### The literal German, by manuscript line

This preserves the transformation’s letters, line breaks and unresolved insertions. [patch] marks the cancelled place, although it consumes no retained key position.

```text
01  der[43]stehetitzoaufmsprungewollen[45]seinergernlosseinundihn
02  entbehrenkonnenseistesnunzeitdas[LL]schreibenweilsiesehendaserm
03  itdenschwedischengeneralendescommendohalbersichnichtuergleichen
04  wurden[45]estatabererfordertedatsieihretqouppenbeydieschw
05  edenunddieschwedenwiderbeysiestossenmustenauch[LL]acti
06  onesihmenitmergefielenunduberdasihmesolcheabsolutege
07  waltwieerbegertenitgebenkontensostelletensieesdahin
08  wa[patch]sihmezuthungefelligwoltenihnauchwiderseinegelege
09  nheitnitaufhaltensondernihnnachihremitzigdnestatundm
10  oglichkeitcontentirenlassen
```

### German with editorial spacing

Only spacing, punctuation and capitalization have been added. The difficult forms remain exactly as decoded.



Der [43] stehet itzo aufm Sprunge; wollen [45] seiner gern los sein und ihn entbehren konnen. Seist es nun Zeit, das [LL] schreiben, weil sie sehen, das er mit den schwedischen Generalen des Commendo halber sich nicht uergleichen wurden. [45] Estat aber erforderte, dat sie ihre tqouppen bey die Schweden und die Schweden wider bey sie stossen musten. Auch [LL] Actiones ihme nit mer gefielen, und uber das ihme solche absolute Gewalt, wie er begerte, nit geben konten. So stelleten sie es dahin, wa[patch]s ihme zu thun gefellig; wolten ihn auch wider seine Gelegenheit nit aufhalten, sondern ihn nach ihrem itzigdn Estat und Moglichkeit contentiren lassen.



The three conspicuous blemishes are `seist`, `tqouppen` and `itzigdn`. Proposed readings such as “so ist”, “trouppen” and “itzigen” are editorial conjectures. `dat` is also retained; it may be historical or dialectal. The sequence `estataber` has been spaced as “Estat aber”, without replacing its letters with “es hat aber”. A clean translation must not quietly rewrite the evidence it is supposed to explain.

## Reproduce the 510-letter transformation

This Python 3 snippet contains the complete normalized input. It checks its hash, decrypts it, checks the exact literal output against the recorded hash, and re-encrypts it. The diplomatic markers and patch are recorded above; they are intentionally absent from this letter-only input.

```python
from hashlib import sha256

alphabet = "abcdefghiklmnopqrstuwxyz"
shifts = (4, 5, 3, 6, 2)  # EFDGC; a = 0
ciphertext = "".join("""
hkuzwinhalyergxkrwwtzsklysqolpxkmtgwmhypptwzgnsytfnnqlpyghotisnu
prkqzgnyxluraqfgnzgguxhlygnghtyioozliyhogridzgwrmafiswikakgpugnh
tiishycpkqkgxhrsoisgukeqeltxofopnhlaxixkrgnhllpaaukgrkwacyfeltix
iuthkuaghfxzliolygywrbrtkqhgcimlugnzlfisytfhohzembhkgrbmkgwgheun
kwaqxyhtozyxlpeafocgzmupiymooismaoixklhnkolpzsgbdixggunnplusqfog
egwunzzhngafoaynkhydimhywismaiightmssxlpxtwagpqhagrymlgxidolrbdz
lmrhfxynytiilhrnnmzunykqpkrfyikaogltxkmtglkoliislllysmaczllgnykq
zqrihypnnqtcgnmotirmabnmgtgxzdaxripuipofomioxiqrzhtwnxhtneywlp
""".split())
assert len(ciphertext) == 510
assert sha256(ciphertext.encode()).hexdigest() == (
    "c9fd887a1db86f327b5d68cc0ad3bdaff27356e37bf142b0d056f95ae2460d29"
)
plain = "".join(
    alphabet[(alphabet.index(c) - shifts[i % 5]) % 24]
    for i, c in enumerate(ciphertext)
)
assert sha256(plain.encode()).hexdigest() == (
    "16f6843b74bd7703d2ad64129a795c863e753904af7d6c5f590cbd54e952f10d"
)
encoded = "".join(
    alphabet[(alphabet.index(c) + shifts[i % 5]) % 24]
    for i, c in enumerate(plain)
)
assert encoded == ciphertext
print(plain)
print("510 letters; expected plaintext hash; 0 re-encryption errors")
```

This small reproduction checks the transformation, not the image-reading decisions or the statistical discovery. The [research text and code package](https://maxim-egorov.dev/research/malsburg-1637-text-and-code.zip) contains the glyph ledger, variant ensemble, protocols, independent implementation and source-position alignment. Archival images are excluded; use the credited source-image link above.

### Statistical checks and deviations

The statistical review has limits too. Two disjoint runs of 4,999 shuffled streams found no exceedance of the declared global period-test maximum, giving a plus-one permutation p of 0.0002 in each run. That comparison is conditional on a randomized-order null and the stated test family; it is not a probability that the plaintext is wrong. Earlier exploration is outside that correction. An adjacent-seed rerun shared nearly all its draws and was not independent; the decoding branch also opened before the genuinely disjoint replication finished. The package records both deviations. Autocorrelation was borderline across runs and is not offered as a separate confirmation.

### Input and code fingerprints

These are SHA-256 hashes. Text-file hashes include the files’ final newlines; the two string hashes in the snippet exclude whitespace.

| Artifact | SHA-256 |
| --- | --- |
| Original archival JPEG | `52811d32eaa8ca7192c8dd985b90a9806a700b4d0b5a337edee4c60f4d0c7535` |
| Frozen initial transcription | `c227593279313d692ee2f53f97fda2c8702b8b51c4c55574112f94f335dd412c` |
| Reviewed visual reading v2 | `cd2304a9e6bd3b51e9a2d0f52d5a39620e3b648f1b834bf3e5e633ae456271be` |
| Reviewed variant ensemble | `3025f452048837e5b4053278082f937f62029f62206b2df515727d37ae58f86e` |
| Normalized ciphertext file | `4a6444d0bdd9b1da52ecd3b4361d34d79f95457720e0a8854eb2dbe2144449ae` |
| Literal plaintext file | `872c9ea8dccfd921c5f95b489c9fbd62b2bd3436a2988fd37080cbc1f8c0e556` |
| Independent decoder file | `fafd8514f48fb6e5487fee97f320b42d25e3858d6bde56e89eec3b45198605c3` |

## What remains open

External historical and paleographic verification of this article’s reading remains pending. The original edition recorded a request for verification from Daniel Bourdeau. The later contribution to his repository, noted above, should not be treated as a response to that request or as external validation of our image-reading decisions.

We still need to explain the markers, assess the local blemishes and examine the cancelled material as a source problem. The exact choice of bare or marked `u` is not resolved by the cipher, because both normalize to the same letter.

This dated account documents our result and makes it inspectable. It does not establish global priority or claim that nobody read the block before us. It also does not claim to solve every cipher in Malsburg’s correspondence. The engineering lesson is concrete: preserve uncertain inputs, inspect where their errors come from, and make a promising result survive checks that are capable of finding it wrong.

