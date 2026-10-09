# Malsburg’s cipher letter (1637)

A separate ten-line alphabetic cipher block at the foot of a January 1637 letter attributed to Malsburg. This investigation covers that block, not the whole surrounding numerical correspondence.

## What has been found?

A repeating sequence of five shifts gives a sustained German reading about command, Swedish generals and possible departure. The proposal reproduces all 510 retained normalized letters, but damaged wording and the people behind several markers remain unresolved.

A small example from the recorded result:

```text
h k u → d e r
```

The first three recorded cipher letters become the German opening der under the saved five-shift rule. That small example can be checked by hand.

## Research update — 9 October 2026

Read the [new check and its limits](research-updates/2026-10-09-numerical-codes.md). This update is documentation; new experiment scripts are not included.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [German reading with manuscript markers](verification/readings/evidence/Malsburg_1637_evidence_and_code/Malsburg_1637/cryptanalysis/diplomatic_decipherment.txt) to inspect the saved text or test result itself.
3. Read the [research account](malsburg-1637/article.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/497); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

510-letter alphabetic-block reading proposal. Unresolved markers, literal defects and missing historical alphabet.json remain explicit. Daniel Bourdeau’s foundational work and Larry Beck’s later contribution with ChatGPT are credited in the research account.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/malsburg-cipher-letter-1637/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
