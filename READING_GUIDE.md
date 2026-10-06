# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A separate ten-line alphabetic cipher block at the foot of a January 1637 letter attributed to Malsburg. This investigation covers that block, not the whole surrounding numerical correspondence.

Start with the [source catalogue or manuscript](https://crypto.hcportal.eu/dashboard/cryptograms/497). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

A repeating sequence of five shifts gives a sustained German reading about command, Swedish generals and possible departure. The proposal reproduces all 510 retained normalized letters, but damaged wording and the people behind several markers remain unresolved.

Open [German reading with manuscript markers](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/diplomatic_decipherment.txt) and the [research account](malsburg-1637/article.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
h k u → d e r
```

The first three recorded cipher letters become the German opening der under the saved five-shift rule. That small example can be checked by hand.

The German remains defective at points, and unresolved markers do not identify particular people. Re-encrypting the result checks consistency, not unique historical correctness. The original statistical search is not reproduced by this public replay.

## Check one example by hand

1. Read the [24-letter alphabet and key rule](malsburg-1637/article.md#one-alphabet-one-key-one-continuous-stream): `abcdefghiklmnopqrstuwxyz`. Count from zero: `a=0`, `b=1`, and so on in this exact alphabet, which omits `j` and `v`.
2. Subtract the repeating shifts `4, 5, 3, 6, 2` from successive cipher-letter indices; wrap around modulo 24.

| Position | Normalized cipher | Zero-based index | Subtract | Output |
| --- | --- | --- | --- | --- |
| 1 | `h` | 7 | 4 | `d` (3) |
| 2 | `k` | 9 | 5 | `e` (4) |
| 3 | `u` | 19 | 3 | `r` (16) |

3. Check the same three rows in the [alignment ledger](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/independent_validation/independent_glyph_alignment.csv). The source shape labelled `ü` is normalized to `u`; this is a recorded convention, not a new historical identification.
4. Compare with the [manuscript image](https://api.hcportal.eu/media/1395/79511677516420.jpg). Numbers `[43]`, `[45]`, the angular `[LL]` and a cancelled patch are retained in the [diplomatic reading](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/diplomatic_decipherment.txt) but do not consume key positions in this model. The shifts continue across line breaks; they do not restart at each row.

Daniel Bourdeau’s source/transcription work and Larry Beck’s later contribution with ChatGPT are credited in the research account. Recorded publication timestamps are not proof of discovery priority or dependence.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/malsburg-cipher-letter-1637/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](malsburg-1637/article.md) | Historical context, method, interpretation, credits and limits |
| [German reading with manuscript markers](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/diplomatic_decipherment.txt) | The saved text or bounded test result |
| [Per-letter shift and alignment](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/independent_validation/independent_glyph_alignment.csv) | The recorded input/assignments used in the example |
| [Alphabet and five-shift rule](malsburg-1637/article.md#one-alphabet-one-key-one-continuous-stream) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
