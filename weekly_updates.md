# Week 05
## 2026-10-05 - 2026-10-10
## Work Streams Schedule Week 05
> [!NOTE]
> *See course outline for stream completion rubric* (i.e., completion of green cells 🟩 vs others & how they accrue).
- [] Administration: Revise REB 🟩

**Status**: 

### 2026-10-10
### 2026-10-09
### 2026-10-07
**Post-Meeting Plan**
1. Next steps for [linglit](https://github.com/haberchr/langlit): Use existing fst in *langlit* with bare-minimum lexicon and affixation to (i) understand how it works with current grammar and (ii) figure out efficacy as UI tool for parser.
2. Extended trial-and-error setting up wsl will continue on this next week.
3. SFU server space was accessed, better idea how to use it as hosting space.
4. Will tackle H-deletion rules as next rule-based challenge.
### 2026-10-06
1. Continued playing around with [linglit](https://github.com/haberchr/langlit) ...
   - Challenge is that the lexc files are formatted very differently (e.g., dictionary is combined with categories vs as roots as .csv and then different files for the categories ...)
   - Conversion to this format will be time-consuming, and I am not sure how to layer the different affixes (e.g., suffixes vs clitics) in the fst so that incorrect combinations don't arise OR could be glossed
      - Good question for linglit team! 💭❓🤔
2. But, I think an MVP is very possible with staging on my SFU server space. 

> [!NOTE]
> No progress on REB since I haven't heard back from community partners yet. Need to work on informed consent forms in meantime.

> [!IMPORTANT]
> Have not heard from community partners, but have connected with CForbes a bit. Can ask her for temperature check about workflow and commitments in community.

# Week 04
## 2026-09-30 - 2026-10-4
## Work Streams Schedule Week 04
> [!NOTE]
> *See course outline for stream completion rubric* (i.e., completion of green cells 🟩 vs others & how they accrue).
- [X] Administration: Identify venue for publication

**Status**: Completed

- [X] Testing: Test phi features

**Status**: Completed

- [X] Rewrites: Fix 3 paradigms

**Status**: Completed (fixed like 8+!) 

- [] Frontend: Develop front end for deployment - basic web formatting, audio 🟩

**Status**: Partial

- [] Community contact: Negotiation of server venue 🟩
      
**Status**: 

### 2026-10-04
1. Thinking through, I do not think there any other features I need to specify in the phonology for the parser as is. Ultimately, it is an ongoing process since if something does arise and code starts to break, then I need to return to it. Otherwise, I think I can put a pin in it.
2. Identified two potential journals and one immediate conference (and three far off ones) for research publication/presenation:
   - Potential journals:
     - [Linguistic Issues in Language Technology (LiLT)](https://journals.colorado.edu/index.php/lilt/about)
       - Small journal, but applicable in scope of current work.
     - [Computer Assisted Language Learning](https://www-tandfonline-com.proxy.lib.sfu.ca/journals/ncal20)
       - Larger journal, could address broader CALL efforts for language.
   - Potential conference(s):\
      **Immediate**
     - Canadian Association of Linguistics (CLA) [annual conference 2027](https://cla-acl.ca/congres-annuel-annual-conference.html)
   - Potential conferences:\
      **Far Off**
     - ComputEL-11 (2028) ... wherever that may be (likely coordinated with ACL Conference) ...
     - Language Documentation and Archiving [LD&A 2028](https://langdoc.org/)
     - Society for the Study of the Indigenous Languages of the Americas [SSILA 2028](https://www.ssila.org/en/home) ... wherever that may be ...
       
### 2026-10-03
1. Began playing around with [linglit](https://github.com/haberchr/langlit) to test applicability.
   - As expected, it is a bit more complicated beneath the surface. The grammar will take a bit to integrate into the 'dummy' directory.
   - The repo is cloned locally anyways.
   - Will need assistance on how to make a virtual environment to test functionality/ UI.
   - Should I add to my Github? This cloned repo? I feel **not** since it is barely work-in-progress.

### 2026-10-02
![Alt Text](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGV5eHltZHpyaW1tNmN5dnM0dTcwNWNla2xmcWtlY2p1NjE2NXYyeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3zFcbgHoIXzykQc7vU/giphy.gif)

1. Somewhat solved the interrupting glottal issue! Issue was that roots with interrupting glottals must be dealt with on LHS -> RHS, not LC _ RC!
   - Contexts are highly specialised to environments of given floating glottals. Very loose patterning since some interrupting glottals predict different interruptions (e.g., {a'a} -> [ {a'a} | {aa'} | {a'} ] || _ t vs {a'a} -> [ {a'a} | {a'} ] || _ [ Sonorant | {x_} | {k_} ]
     - Fun fact: this is sort of predicted in the phonology of the language too since some linguists believe a lot of irregularities are simply learned individually by speakers in Maritime Tsimshianic languages based loosely on phonological environments.
   - Issue now is overgeneration of bare root, but raises question as what is acceptable as 'bare root' really?
   - Some overgeneration exists for superficially identical phonological environments with a glottal that does not move.
   - Some vowel tests, need to review to see if paradigm is accurate since in comparison to glottal tests, results still are errors and may not predict accurate expected results.
   - H-deletion with o: *noh* *no* still issue, but think can be adjusted with similar root rewrite rule
2. Error rate down to (n=46)! 🙌📉💞

# Week 03
## 2026-09-22 - 2026-09-26 (Extension to: 2026-09-29 RE: Yom Kippur🕯️📖)

## Work Streams Schedule Week 03
> [!NOTE]
> *See course outline for stream completion rubric* (i.e., completion of green cells 🟩 vs others & how they accrue).
- [X] Administration: Reach out to Nathalie, formalize TouchCounts interest 

**Status**: Completed

- [] Rewrites: Fix glottalisation/incorporating phi features 🟩

**Status**: Partial / Ongoing[^3] 

[^3]: Feature incorporation is for the most part finished. I will update and add more details (as applicable to testing). Main changes were specifying glottalisation as distinct, which I think will serve us well in the future and is key to fixing interrupted glottal rule(s). Otherwise, vowel features were updated too, which support concise feature-based rule-writing.

- [] Frontend: Learning the final server environment
  
**Status**: 

### 2026-09-28
1. Fixed mid-hanging fruit tests and errors.
   - Completed all cluster tests! Woohoo! 🎉
   - H-deletion tests somewhat successful 😕
     - Issues persist: (i) accent is not incorporated yet, so all tests that require marked stress fail DESPITE correct strings and (ii) H-deletion and -t from -3.II is having issues with optional deletion.
   - Error rate now (n=124).
2. Glottal tests now main blocker for development 🎯🧐🧠
> [!Important]
> Traditional rites are being held due to passing in community.

### 2026-09-26
1. Fixed low hanging fruit tests and errors.
   - Some errors were because expected output was incorrect upon review. Testing helped identify where I made errors on some predictable sound changes (i.e., mostly voicing and -sm epenthesis).
   - Except Rules were tested but unsuccessful. Test-case was SX_ cluster that does not harden (i.e., sx̠ -> *sg̠).
   - i-Deletion rule may cause issues in future with interrupted glottals, but will cross that bridge later ...
   - Currently only H-final vowels, interrupting glottals, and SX_ cluster errors persist. 
   - Error rate now (n=131).
2. Draft response to send NSinclair for tomorrow 2026-09-27.
### 2026-09-25
1. Emailed NSinclair for TouchCounts inquiry.
   - Received positive response. App will be on App stores soon too. Can send specs for what to record. Varies by language & regularity.
2. Emailed community partners as check-in RE: research proposal.
   
### 2026-09-23
1. Meeting with SNg
   - Generally successful. Figured some steps for optional glottal rules & glide-insertion.
   - Somehow broke VisualStudiocode, so now cannot test individual paradigms. Need to fix.
   - Pivot to using foma more, but issue persists with [0] no input once load.
2. Updated dictionary with new test words.

> [!TIP]
> Test output problem solved ... after ***three hours*** ...
   
3. Issue with VisualStudiocode was in settings.json "test*.py" was ***test.py**, which made all tests unfindable. Fixed and saved; will monitor and narrow in on this .json of issue continues.
4. Error found in stress marking for 'dahdee', so error rate is now (n=148). GlideInsertion rule is not successful.

# Week 02
## 2026-09-14 - 2026-09-19 
## Work Streams Schedule Week 02
> [!NOTE]
> *See course outline for stream completion rubric* (i.e., completion of green cells 🟩 vs others & how they accrue).
- [] Administration: Submit REB 🟩

**Status**: Partial / Ongoing

- [X] Testing: Identify issues in output formatting

**Status**: Completed / Ongoing

- [] Rewrites: Fix glottalisation/incorporating phi features 🟩

**Status**: Partial / Ongoing

- [] Frontend: Test goodness of fit of identified systems

**Status**: Partial

- [X] Community contact: Orthography: discuss and find way to accommodate variation [^2]
      
**Status**: Completed
[^2]: Orthographic variation was discussed at the initial discussion 2025-08-25 & subsequently via email. Multiple entries will be added as expected Output in the meantime as spelling differences are resolved.

### 2026-09-19
1. Merged DeletePGM & GlottalMove into one rule GlottalMove1, GlottalMove2, etc. respective of vowels (n=4). No change to 163 error rate no matter where they are moved.
   - Confused by this. Parser is working since removing other rules causes massive spike in failures. Something possibly to do with the optionality that makes these rules inconsequential?
2. Debugged parser tests (incorrect syntax in new tests).
   - Error rate now (n=156).
3. Some distinctive features added to phonology rules (nasals, +high, +back, +front, +cg (i.e., glottalised)).
   - Will *slowly* incorporate into rules rewrite. Rather not throw out the baby with bathwater since most of fst works alright. Can discuss workflow later. 
4. Got side tracked from **Test goodness of fit of identified systems** looking out how to do pretty_paradigm fst command. Draft is [uploaded](https://github.com/gitbenchung/sguuxs_splicer/blob/ling_896/src/parser_test_01_LING986.py). Need assistance at certain intervals, but I have the pipeline identified.
5. Haven't heard back from community partners RE: proposal. Will follow up next Tuesday, 2026-09-22.
6. Looked into designated front-end sandbox space using sfu ID.
   - I downloaded the right file manager/file transfer client. Not sure if it was the IT issues last week affected my view and functionality via VPN. Interested in discussing management and deployment at next check-in.
   
### 2026-09-18
1. Adapted pronoun system in full_sgx for be Sgüüx̱s not Gitksan. Less necessary now for nominal morphology, but better consistency in labeled files to have Sgüüx̱s *be* Sgüüx̱s.
2. Rule ranking tests: DeletePGM lower and DZVoicing higher (=163 errors) vs DeletePGM higher and DZVoicing lower (=168 errors).
   - Issues with optional rules, dz-voicing. Need to make specific rules for phonological effects for clusters. 
3. Given how [linglit](https://github.com/haberchr/langlit) is set up: (i) will try to link UI to existing sgx_splicer infrastructure to feed into pipeline to tests (and if that fails (ii) input sgx_splicer test data into cloned *langlit* to try to get UI functional.
   - Other CALL tools not explored genuinely explored yet.

> [!WARNING]
> Need to devote time to make python code for pretty paradigms! Add to docket for next week.

### 2026-09-17
1. Updated 1 misplaced test 'sand fleas' in wrong TestClass.
2. Experimented with rule word order / tried separating moving glottal rule and interrupted vowel deletion into different rules.

### 2026-09-16
1. Completed upload of 19 tests.
   - 5 updated tests (vowels).
   - 14 new tests (plain l, stops, clusters and vowels).
     - Multiple errors mostly with Y-insertion, H-Deletion & potential glottal movement (may not apply when in open syllable, flagged).
   - Multiple glottal entries added. Non-H deleting nouns like *nanah* 'duck' will be excluded from parser for now.
     
### 2026-09-14
1. Connected with MIgnace about research proposal.
2. Research proposal official document sent to KXN community partners for review.
3. Learned that [ComputEL-10](https://computel-workshop.org/computel-10/) has submissions until 2026-10-02 for conference next March 2027.
   - Will discuss with SNg about applicability given our current timelines.
4. Deleted 3 irrelevant cluster tests; updated 16 additional tests.
   - 11 new cluster tests updated/added.
   - 1 plain consonant test added.
   - 4 non-cluster tests updated.

# Week 01
## 2026-09-06 - 2026-09-12 (Extension to: 2026-09-14 RE: Rosh Hashanah 🍎🍯)
## Work Streams Schedule Week 01
> [!NOTE]
> *See course outline for stream completion rubric* (i.e., completion of green cells 🟩 vs others & how they accrue).
- [] Administration: Submit REB 🟩

**Status**: Partial

- [X] Testing: Identify all paradigms and their status 🟩

**Status**: Complete

- [X] Rewrites: Clean existing code base

**Status**: Complete

- [X] Frontend: Research existing CALL repos relevant to morphophonology

**Status**: Complete, literature review (lit review) technically ongoing 📚

- [X] Community contact: Discuss with community partner(s) test cases/ application of FST [^1] 🟩
      
**Status**: Complete

[^1]: Meeting with AEdgar and CForbes took place 2026-08-25 to discuss these topics. Currently research proposal for Stewardship Department is in draft based on this discussion.

### 2026-09-13
1. Initial draft of REB complete.
   - Need to check about Data Security & Confidentiality language with SNG (maybe MIgnace).
   - Need to work on recruitment forms (i.e., informed consent documents).

### 2026-09-11
1. Read 1 CALL article > found useful UI built for fsts with UDUB connections [linglit](https://github.com/haberchr/langlit)!
2. Meeting with SNg. Discussed:
   - 'pretty paradigm' function and end product > added as task.
   - langlit and potential meeting with team RE: functionality and natural language test-cases in October.
   - Ethics application and community partnership agreement timeline.
   - CALL reading task; can be marked as 'completed' as enough has been reviewed to give solid directions, but lit review is ongoing.
3. Personal SFU-secured server space for demo is in works.
   - Downloaded WinSCP; will troubleshoot set-up next week.
   
### 2026-09-10
1. Got response from CForbes on questions. Much guidance.
   - Idea about code to generate 'pretty paradigms' from test results via CForbes.
2. Set of paradigms for testing finalised.
   - Tests to make: 13.
   - Tests to create: 22.
3. Removed non-essential files from repo. Clean existing code base is complete to my satisfaction.
4. Explored possibility for 'pretty paradigm' function in parser.py. Possibly tabulate but also pandas.
   
### 2026-09-09
1. Read four articles in Zotero RE: CALL
   - 15+ articles were added 09-08. 

### 2026-09-08
1. Double-checking existing code-base for redundancies/ ensuring merges are synced for testing.
2. Communication with SNg & MTaboada for worklog.
3. Added status section for worklog.
4. Read three articles in Zotero RE: CALL
   - Planning to add to library Wed-Fri
   - Aim is 20+ articles with 10 total reviewed by Sat
   
### 2026-09-07
1. Went through sound change spreadsheet and recategorised contexts.
   - Sent email to CForbes on missing vocabulary and vowel tests.
2. Made new branch for directed research. Will update this branch during course/ will act as new dev.
