# Independent check of Sneiderman's r = 6 and r = 7 cases of Erdős Problem 617

[Erdős Problem 617](https://www.erdosproblems.com/617) (Erdős–Gyárfás) asks whether, for every r ≥ 3, every r-colouring of the edges of K_{r²+1} has r+1 vertices whose induced edges miss a colour.

Robert Sneiderman has posted proofs of the fixed cases r = 5, …, 9 in [`Robby955/erdos-617-fixed-cases`](https://github.com/Robby955/erdos-617-fixed-cases). This repository records an independent check of two of them:
- **r = 6:** `r6/main.tex`, in full;
- **r = 7:** Sections 2–4 of `r7-r8/main.tex`.

The check was made at commit `fb628c8` of Sneiderman's repository.

## Who we are

- **Gael Irambona**, master's student in philosophy at the Université de Picardie Jules Verne (France). He is not a professional mathematician.
- **Claude**, an AI assistant made by Anthropic, which did most of the mathematical checking.

A separate Claude session, with no access to our working notes, re-checked the audit. That makes it a second pass by the **same AI system**, not a third party. No human mathematician has reviewed this work. Please read it as one more independent check, **not as a referee report**.

## Results

| | Status |
|---|---|
| r = 7 | Human-readable chain re-derived step by step without code (by Claude); no mathematical error found beyond the written repair already posted by nwinter's agents (see below). |
| r = 7 computed inputs | Recursion values reproduced by our own reimplementation; the finite lemma (Lemma 3.2) re-implemented independently. |
| r = 6 | Redone by hand. Everything we found there **was already known** (see below). |

### What was already known

- **r = 6** was reviewed earlier by Nick Winter's project ([`nwinter/erdos-617-r5`](https://github.com/nwinter/erdos-617-r5), `reviews/sneiderman-r6.md`, 29–30 July 2026). That project also formalized the r = 6 theorem in Lean, by its own proof (not a check of Sneiderman's manuscript). Its review already contains the two r = 6 points we reached:
  - Lemma 2.3 (the Kang–Pikhurko equality endpoint) is removable;
  - "nonbipartite" at `r6/main.tex` line 403 needs one line of justification.
- **r = 7, 8, 9** were screened by nwinter's agents. Their comment on the forum's r = 9 claim (31 July 2026) asks for two written repairs:
  - the inference at `r7-r8/main.tex` line 403, with a three-step repair;
  - the eight-set-cap sentence at line 642, which belongs to the δ = 7 branch only.

  **Our pass had not flagged either point.** We confirm both on re-reading.

### Our own remarks (not claimed as new)

1. **For r = 7, the m = ar+1 passage is not load-bearing.** The Kang–Pikhurko *equality* characterization enters the r = 7 proof only through the "+1" in the third line of Q_r. Dropping that "+1" changes:
   - no value B₇(a, m) with a ≤ 6 and m ≤ 49;
   - nothing in the margin table;
   - none of the input floors 63, 75, 143, 153, 176.

   Run `kp_equality_check.py` to see this. So at r = 7 only the Kang–Pikhurko *inequality* is used. We offer this as a complement to the repair above, not as a replacement for it. We did not check it for r = 8 or r = 9. We did not find this remark in the sources we could read, but the full r = 7, 8, 9 screen by nwinter's agents is not public, so it may already be there.
2. **A short alternative proof of the level-3 exclusion (T₃ = 1)** that uses neither Theorem 2.2 nor the hypothesis ω ≤ r − 1. It is in Section 3 of the audit PDF. It uses the same method as Sneiderman's Theorem 2.2 ("maximum degree + strict coloured density"). It is an independent check, not a new method.
3. **An independent re-implementation for Lemma 3.2** (weighted light edge), following the same idea as the author's Sage route but with networkx instead of nauty. It enumerates the networkx atlas of all unlabelled 7-vertex graphs and recovers labelled counts as 7!/|Aut|. It gives the same 40 / 65 / 97 / 131 graph types, the same labelled counts and the same table of extrema as the author's two checkers.

## Contents

```
audit_r6_r7.pdf             the audit (LaTeX source: audit_r6_r7.tex)
ladder.py                   reimplementation of the thresholds T_s, the recursion B_r(a,m) and the margin table
kp_equality_check.py        Observation 2: recomputes everything without the Kang–Pikhurko equality "+1"
light_edge.py               independent re-implementation of the r = 7 finite lemma
SHA256SUMS                  checksums of the files above
```

## How to run

You need Python 3.9 or later, and `networkx` for `light_edge.py`. Each script runs in about a second.

```bash
pip install networkx
python3 ladder.py 7              # thresholds {2:0, 3:1, 4:2, 5:5}, margin table, floors 63 75 143 153 176
python3 kp_equality_check.py     # "values that change: none", "margin table identical: True"
python3 light_edge.py            # types {6:40, 7:65, 8:97, 9:131}; (i) True, (ii) True
```

`ladder.py` was written from the text of Sneiderman's consolidated draft, not from his code. Please keep r ≤ 9 when running it.

## Limits

- Lemma 3.2 and the recursion values were checked by machine only, not by hand.
- We relied on the published statement of the Kang–Pikhurko theorem and did not re-read their paper.
- We did not check r = 8, r = 9, or the SAT/LRAT certificates.
- Our pass missed two wording issues that nwinter's agents had found earlier. It should not be read as more thorough than theirs.

## Credits

- The proofs audited here are Robert Sneiderman's.
- The prior reviews cited above are by Nick Winter's project and its agents.
- Mistakes in this repository are ours.

## License

The code is released under the MIT License (see `LICENSE`). The text and the PDF are shared under CC BY 4.0.
