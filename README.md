# Evidence Note Generater（エビデンスノートジェネレータ）

クリニカルクエスチョンに対してエビデンスを探索した上でノート（日英対応）を作成するCodex Skills。　　
Codexをルートディレクトリで開いて臨床における疑問点を入力すると/output下にevidence noteを作成する。  

markdownのビューワとしては/outputディレクトリをObsidianのVaultとして読み込むことを推奨。  
<img width="2879" height="1824" alt="image" src="https://github.com/user-attachments/assets/956a01a7-f0cf-427a-aca2-7dec79523778" />

## 作成例
### 質問例
User Prompt：小児ネフローゼ症候群の浮腫に対する治療について

### 出力例（日）
```markdown
# 小児ネフローゼ症候群の浮腫に対する治療
## Clinical question
小児ネフローゼ症候群において、浮腫をベッドサイドでどのように評価し、食塩制限、飲水制限、ループ利尿薬、静注アルブミン、あるいは急性循環血漿量補正をどのように使い分けるべきか。

## Bottom line
- 浮腫治療は、まず volume status の評価から始めます。高度浮腫があっても、実際には血管内容量が低下していることがあり、この見極めが利尿薬の適否を左右します [1-4]。
- 軽度から中等度の浮腫は、通常はネフローゼ状態そのものの治療と食塩制限で対応します。ルーチンの飲水制限は推奨されません [1,3]。
- ループ利尿薬は、低循環血漿量が否定された重度浮腫で選択的に用います。体重、尿量、血圧、Cr、電解質の近接モニタリングが必要です [3,4]。
- 静注アルブミンは routine therapy ではありません。重度浮腫で、有効循環血漿量低下が疑われる場合や利尿反応が乏しい場合の選択肢ですが、小児の直接エビデンスはかなり乏しいです [3-6]。
- 低循環性ショックや明らかな血管内容量低下がある場合は、まず循環を是正します。単純な fluid overload と誤認して利尿をかけると、AKI、血栓、ショック悪化を招き得ます [3,4]。

## Why this matters
浮腫は小児ネフローゼ症候群で最も目につきやすい症状であり、入院理由にもなりやすい一方、ベッドサイドでの判断ミスが起きやすい問題です。同じ「全身がむくんだ」患児でも、実際には有効循環血漿量が低い場合と、Na 貯留主体の fluid overload の場合があります。この病態整理を誤ると、AKI、肺水腫、血栓症、ショック遷延といった有害事象につながります [3-6]。しかも、小児での比較試験は限られており、系統だった臨床推論が重要です。

## Scope and intended use
本ノートは、小児ネフローゼ症候群に伴う浮腫の支持療法に焦点を当てた resident 向け実践ノートです。国際ガイドラインと、小児でのアルブミン/利尿薬使用に関するレビューを中心にまとめています。実際の浮腫治療に関する強い推奨の多くは、特発性・ステロイド感受性ネフローゼ症候群の文献に基づくため、その領域が議論の中心です。免疫抑制治療の全体像や二次性ネフローゼ症候群は主な対象外です。

## Key definitions
- 小児ネフローゼ症候群: 高度蛋白尿、低アルブミン血症、浮腫を主徴とする症候群で、小児では特発性が多い [1,3]。
- 低循環血漿量 / intravascular depletion: 全身としては体液過剰でも、有効循環血漿量が不足している状態。ここで安易に利尿薬を使うと危険です [3,4]。
- overfill physiology: 腎での一次的 Na 貯留が主体で浮腫が形成される状態で、低循環血漿量が否定できれば慎重な利尿が有用となり得ます [4]。
- 重度浮腫: 全身性または緊満性の浮腫で、著明な不快感、歩行障害、腹水、陰嚢/陰唇浮腫、胸水、呼吸苦などを伴い、入院管理を要し得る状態 [3,4]。
- albumin-assisted diuresis: 静注アルブミンに、しばしばフロセミドを組み合わせて、一時的に血管内容量を増やし利尿反応を改善させることを狙う治療 [3-6]。

## Evidence base
### Search strategy
検索日: 2026-04-19.

テーマは「小児ネフローゼ症候群の浮腫に対するベッドサイド治療」に絞りました。まず最新の小児ガイドラインを優先し、その後に小児中心のレビューと、アルブミン治療に関する系統的レビューを追加しました。

主な検索式:
- `"KDIGO 2025 nephrotic syndrome in children edema albumin furosemide"`
- `"IPNA steroid-sensitive nephrotic syndrome edema albumin fluid restriction children"`
- `"mechanisms and management of edema in pediatric nephrotic syndrome review"`
- `"human albumin infusion nephrotic syndrome children Cochrane"`
- `"intravenous albumin oedema children nephrotic syndrome systematic review 2025"`

### Included evidence
1. KDIGO 2025 小児ネフローゼ症候群ガイドライン [1]。
2. KDIGO 2025 executive summary [2]。
3. IPNA 2023 のステロイド感受性ネフローゼ症候群臨床推奨 [3]。
4. 小児ネフローゼ浮腫の機序と管理に関する 2021 年レビュー [4]。
5. ネフローゼ浮腫に対するヒトアルブミン投与の 2019 年 Cochrane review [5]。
6. 小児ネフローゼ症候群に対する静注アルブミンの 2025 年系統的レビュー [6]。

### Excluded / deprioritized evidence
- 成人ネフローゼ症候群の浮腫レビューは、小児へそのまま適用しにくいため除外しました。
- 再発予防、steroid-sparing therapy、ステロイド抵抗性ネフローゼ症候群の治療比較試験は、今回の問いが症候性浮腫治療であるため優先度を下げました。
- 浮腫管理に関する追加情報が乏しい総説は、KDIGO/IPNA を優先して採用しませんでした。

## What is known
### Pathophysiology / background
小児ネフローゼ症候群の浮腫は、単に低アルブミン血症だけで説明できません。血漿膠質浸透圧低下に続く二次性 Na 貯留を主体とする underfill と、腎での一次的 Na 貯留を主体とする overfill の両方が関与し、同じ患児でも時間経過で揺れ動きます [3,4]。したがって、見た目の浮腫の強さだけでは血管内容量は判断できません。浮腫への支持療法は、蛋白尿寛解を目指す原因治療の代わりではなく補助です [1-4]。

### Diagnosis / assessment
最初に考えるべきは、その患児が intravascularly depleted なのか、十分に保たれているのか、あるいは真の fluid overload なのかという点です [3,4]。これは一回決めたら終わりではなく、繰り返し再評価します。

低循環血漿量を示唆する所見 [3,4]:
- 頻脈
- 四肢冷感または capillary refill 延長
- 低血圧または low-normal の血圧
- 乏尿
- Cr 上昇
- 強い腹痛、だるさ、めまい
- 真の低 Na 血症を伴う場合

同時に、浮腫の重症度と合併症も評価します:
- 毎日の体重推移
- 尿量
- 呼吸症状や胸水
- 腹水や緊満した全身浮腫
- 疼痛を伴う陰嚢/陰唇浮腫
- Na、K、Cr、アルブミン [3,4]

軽度から中等度の浮腫では、しばしば原因治療に加えて保存的支持療法で十分であり、過度な浮腫除去は不要です [1,3,4]。一方、重度浮腫では入院下での観察と、選択的なループ利尿薬または albumin-assisted diuresis を考慮します [3,4]。

### Management principles
非薬物療法の基本は、活動性浮腫がある期間の食塩制限です。IPNA は中等度から重度浮腫の間は食塩摂取を制限し、寛解後は通常摂取へ戻すことを推奨しています。ルーチンの飲水制限は推奨されません [3]。飲水制限は、重度浮腫かつ明らかな低 Na 血症がある入院患児で検討されることはありますが、多くの再発での標準治療ではありません [3]。高蛋白負荷で浮腫を改善させることも推奨されません [3]。

軽度から中等度の浮腫では、原則は保存的支持療法です [1,3,4]。つまり、低塩、経過観察、不要な利尿薬を避けることです。IPNA は uncomplicated edema に routine に利尿薬を投与しないよう注意しており、低循環血漿量を見落とすと AKI や血栓リスクを高めるとしています [3]。

重度浮腫で intravascular volume が保たれている場合には、フロセミドなどのループ利尿薬を慎重に用いることがあります [3,4]。その際は以下を近接モニターします:
- 体重変化
- 尿量
- 血圧
- Na、K
- Cr

静注アルブミンは routine intervention ではなく、選択的治療です [3-6]。IPNA では、重度浮腫に対して 20% または 25% アルブミン 0.5-1 g/kg を 4-6 時間で投与し、必要に応じて投与中盤および/または終了時にフロセミド 1-2 mg/kg 静注を組み合わせる方法が示されていますが、marked intravascular contraction や hyponatremia がないことが前提です [3]。理屈としては、一時的に有効循環血漿量を増やして利尿反応性を改善する狙いです [3,4]。ただし、直接エビデンスは乏しく、Cochrane review では小児 RCT は 1 本のみ、2025 年の小児系統的レビューでも routine IV albumin を支持する十分な根拠はないと結論づけています [5,6]。

真の低循環血漿量や低循環性ショックがある場合は、まず灌流回復を優先します [3,4]。IPNA は 4% または 5% アルブミン 20 mL/kg を 20-30 分で投与し、アルブミンが使えなければ等張晶質液を用いることを勧めています [3]。その後に、追加の浮腫治療が本当に必要か再評価します。

浮腫の最も確実な改善は、ネフローゼ状態そのものの寛解に伴って得られます。支持療法だけで決定的に解決することはまれです [1-4]。

### Harms / pitfalls
最大の落とし穴は、すべての浮腫を hypervolemia とみなすことです。低循環血漿量の患児に利尿薬を使うと、AKI や血栓リスクを高め、ショック病態を悪化させる可能性があります [3,4]。アルブミン投与も、尿量が乏しい場合やすでに血管内容量が保たれている場合には、高血圧、肺水腫、fluid overload を起こし得ます [3-6]。

よくある落とし穴:
- 多くの症例で推奨されない routine の飲水制限を指示してしまうこと [3]
- volume status や腎機能を再確認せずに albumin や furosemide を繰り返し増やすこと [3,4]
- 高脂血症に伴う pseudohyponatremia を、過度な飲水制限の理由と誤認すること [3]
- 浮腫そのものに気を取られ、感染、血栓、ステロイド抵抗性、別の浮腫原因を見落とすこと [1,3]

## What remains uncertain
albumin plus furosemide の最適な対象、タイミング、患者中心アウトカムへの影響は、依然として不確実です。小児の比較試験が少なすぎるためです [5,6]。また、underfill と overfill を完全に見分ける単一の bedside test もありません。そのため、浮腫治療の多くは、強い RCT エビデンスというより、ガイドラインと連続的再評価に依存しています。

## Practical takeaways for residents
- まず「この子は intravascularly dry か、adequately filled か、overloaded か」を考えてから利尿薬やアルブミンを出します [3,4]。
- 活動性の中等度から重度浮腫では食塩制限を使い、ルーチンの飲水制限にはしません [3]。
- uncomplicated edema では利尿薬を避け、乏尿、腹痛、Cr 上昇、低血圧があれば特に低循環血漿量を疑います [3,4]。
- albumin plus furosemide は、選ばれた重症例に限って、通常はモニタリング可能な環境で使います。肺水腫、高血圧、電解質変化、Cr 上昇に注意します [3-6]。
- ショックまたは明らかな灌流不全があれば、先に蘇生してから浮腫プランを立て直します [3]。
- 最も持続的な浮腫改善は、支持療法だけでなく蛋白尿寛解に伴って得られます [1-4]。

## Source map
1. Kidney Disease: Improving Global Outcomes (KDIGO) Nephrotic Syndrome in Children Work Group. KDIGO 2025 Clinical Practice Guideline for the Management of Nephrotic Syndrome in Children. Kidney Int. 2025;107(5 Suppl):S241-S289. doi:10.1016/j.kint.2024.11.005. Available at: https://kdigo.org/wp-content/uploads/2025/04/KDIGO-2025-Guideline-for-Nephrotic-Syndrome-in-Children.pdf
2. Floege J, Gibson KL, Vivarelli M, et al. Executive summary of the KDIGO 2025 Clinical Practice Guideline for the Management of Nephrotic Syndrome in Children. Kidney Int. 2025;107(4):806-808. doi:10.1016/j.kint.2024.11.006. PMID: 40254362. Available at: https://kdigo.org/wp-content/uploads/2025/04/KDIGO-2025-Nephrotic-Syndrome-in-Children-Guideline-Executive-Summary.pdf
3. Trautmann A, Boyer O, Hodson E, et al. IPNA clinical practice recommendations for the diagnosis and management of children with steroid-sensitive nephrotic syndrome. Pediatr Nephrol. 2023;38(3):877-919. doi:10.1007/s00467-022-05739-3. PMID: 36269406. PMCID: PMC9589698. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC9589698/
4. Kallash M, Mahan JD. Mechanisms and management of edema in pediatric nephrotic syndrome. Pediatr Nephrol. 2021;36(7):1719-1730. doi:10.1007/s00467-020-04779-x. PMID: 33216218. Available at: https://pubmed.ncbi.nlm.nih.gov/33216218/
5. Ho JJ, Adnan AS, Kueh YC, Ambak NJ, Van Rostenberghe H, Jummaat F. Human albumin infusion for treating oedema in people with nephrotic syndrome. Cochrane Database Syst Rev. 2019;7(7):CD009692. doi:10.1002/14651858.CD009692.pub2. PMID: 31425606. PMCID: PMC6699680. Available at: https://pubmed.ncbi.nlm.nih.gov/31425606/
6. Nawaz SB, Zafar MA. Intravenous Albumin for Oedema in Children With Nephrotic Syndrome: A Systematic Review and Mapping of the Evidence Landscape. Cureus. 2025;17(10):e95142. doi:10.7759/cureus.95142. PMID: 41281089. PMCID: PMC12636047. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC12636047/

## Caveats
本ノートは focused evidence note であり、formal systematic review ではありません。小児の浮腫治療に関する直接推奨の多くは、大規模 RCT ではなく、ガイドラインの合意形成と病態生理に基づく推論に依拠しています [3-6]。また、浮腫治療に関する強い記述の多くは、特発性かつステロイド感受性の小児ネフローゼ症候群から来ているため、二次性ネフローゼ症候群やステロイド抵抗性症例への外挿には注意が必要です。アルブミン治療のエビデンスは特に限定的で、支持されているのは主として短期の生理学的効果です [5,6]。

## Last updated
2026-04-19

```

### 出力例（英）
```markdown
# Treatment of Edema in Pediatric Nephrotic Syndrome
## Clinical question
In children with nephrotic syndrome, how should edema be assessed and treated at the bedside, including when to use salt restriction, fluid restriction, loop diuretics, intravenous albumin, or acute intravascular resuscitation?

## Bottom line
- Edema treatment starts with volume assessment, not with reflexive diuresis. A child with marked edema may still be intravascularly depleted, and that distinction determines whether diuretics are helpful or harmful [1-4].
- Mild to moderate edema is usually managed with treatment of the nephrotic episode plus sodium restriction. Routine fluid restriction is not recommended [1,3].
- Loop diuretics are reserved for severe edema after hypovolemia has been excluded, ideally with close inpatient monitoring of weight, urine output, blood pressure, creatinine, and electrolytes [3,4].
- Intravenous albumin is not routine therapy. It is a selective option for severe edema, especially when effective circulating volume appears low or diuretic response is poor, but the direct pediatric evidence base is very limited [3-6].
- If hypovolemic shock or clear intravascular depletion is present, restore perfusion first. Treating such children as if they were simply fluid-overloaded can worsen AKI, thrombosis risk, and shock physiology [3,4].

## Why this matters
Edema is the most visible complication of childhood nephrotic syndrome and one of the most common reasons for admission, yet it is also a frequent source of bedside error. The same swollen child may have either reduced effective circulating volume or sodium-retentive fluid overload. Misreading that physiology leads to avoidable harm, including AKI, pulmonary edema, thrombosis, and delayed treatment of shock [3-6]. Residents need a structured approach because supportive edema care is common, but high-quality pediatric comparative trials are sparse.

## Scope and intended use
This note focuses on supportive treatment of edema in children with nephrotic syndrome in inpatient and outpatient practice. It is written for resident-level bedside decision-making and emphasizes current international guidance plus pediatric reviews of albumin and diuretic use. Because the strongest edema-specific recommendations come from idiopathic and steroid-sensitive childhood nephrotic syndrome literature, those data anchor much of the discussion. Full immunosuppressive management and secondary nephrotic syndromes are outside the main scope.

## Key definitions
- Pediatric nephrotic syndrome: a syndrome characterized by heavy proteinuria with hypoalbuminemia and edema, most commonly idiopathic in childhood [1,3].
- Hypovolemia or intravascular depletion: reduced effective circulating volume despite total body fluid excess; this is the state in which uncritical diuretic use can be dangerous [3,4].
- Overfill physiology: edema driven mainly by primary renal sodium retention, where cautious diuretic therapy may be useful once hypovolemia is excluded [4].
- Severe edema: generalized or tense edema causing major discomfort, impaired ambulation, ascites, genital edema, pleural effusions, respiratory compromise, or need for hospital-based treatment [3,4].
- Albumin-assisted diuresis: intravenous albumin, often combined with furosemide, used selectively to transiently expand the intravascular compartment and improve diuretic response in severe cases [3-6].

## Evidence base
### Search strategy
Search date: 2026-04-19.

The topic was narrowed to bedside management of edema in pediatric nephrotic syndrome rather than full disease therapy. Search emphasis was placed on current pediatric guidelines, then on pediatric-focused reviews and systematic reviews of albumin-based therapy.

Example search strategies:
- `"KDIGO 2025 nephrotic syndrome in children edema albumin furosemide"`
- `"IPNA steroid-sensitive nephrotic syndrome edema albumin fluid restriction children"`
- `"mechanisms and management of edema in pediatric nephrotic syndrome review"`
- `"human albumin infusion nephrotic syndrome children Cochrane"`
- `"intravenous albumin oedema children nephrotic syndrome systematic review 2025"`

### Included evidence
1. KDIGO 2025 Clinical Practice Guideline for Nephrotic Syndrome in Children [1].
2. KDIGO 2025 executive summary [2].
3. IPNA 2023 clinical practice recommendations for steroid-sensitive nephrotic syndrome [3].
4. 2021 pediatric review on mechanisms and management of edema in nephrotic syndrome [4].
5. 2019 Cochrane review of human albumin infusion for nephrotic edema [5].
6. 2025 pediatric systematic review mapping the evidence for intravenous albumin in children with nephrotic syndrome [6].

### Excluded / deprioritized evidence
- Adult nephrotic syndrome edema reviews were excluded because albumin and diuretic decisions are not directly interchangeable with pediatric practice.
- Trials centered on relapse prevention, steroid-sparing agents, or steroid-resistant nephrotic syndrome were deprioritized because the question here is symptomatic edema treatment.
- Broad pediatric nephrotic syndrome reviews that did not add edema-specific management details beyond KDIGO/IPNA were not prioritized.

## What is known
### Pathophysiology / background
Edema in childhood nephrotic syndrome is not explained by hypoalbuminemia alone. Both reduced plasma oncotic pressure with secondary neurohormonal sodium retention ("underfill") and primary renal sodium retention ("overfill") contribute, and the same child may shift along that spectrum over time [3,4]. That is why the visual severity of edema does not reliably identify the intravascular state. Supportive edema therapy is therefore adjunctive to disease-directed treatment, not a substitute for achieving remission of proteinuria [1-4].

### Diagnosis / assessment
The first practical question is whether the child is intravascularly depleted, adequately filled, or truly fluid-overloaded [3,4]. Reassess this repeatedly rather than assuming a fixed physiology.

Features suggesting hypovolemia include [3,4]:
- Tachycardia
- Cool extremities or prolonged capillary refill
- Low or low-normal blood pressure
- Oliguria
- Rising creatinine
- Significant abdominal pain, lethargy, or dizziness
- Laboratory hyponatremia that fits true water excess or low effective volume rather than pseudohyponatremia

At the same time, assess the severity of edema and its complications:
- Daily weight trend
- Urine output
- Respiratory symptoms or pleural effusions
- Ascites or tense generalized edema
- Painful scrotal or labial edema
- Serum sodium, potassium, creatinine, and albumin [3,4]

Children with uncomplicated mild or moderate edema often do not need aggressive edema-directed therapy beyond treating the nephrotic episode itself [1,3,4]. Severe edema is more likely to justify hospital-based monitoring and selective use of loop diuretics or albumin-assisted diuresis [3,4].

### Management principles
The main nonpharmacologic treatment is sodium restriction during active edema. IPNA recommends limiting sodium intake during moderate to severe edema, with normal intake resuming after remission; routine fluid restriction is not recommended [3]. Fluid restriction can be considered in hospitalized children with severe edema and/or marked hyponatremia, but it is not standard therapy for most relapses [3]. High-protein loading is not recommended as an edema treatment strategy [3].

For mild to moderate edema, the default approach is conservative supportive care while treating the nephrotic episode [1,3,4]. This usually means low-salt intake, monitoring, and avoidance of unnecessary diuretics. IPNA specifically cautions against diuretics for uncomplicated edema because clinicians may worsen AKI or thrombotic risk if hypovolemia is missed [3].

For severe edema with preserved intravascular volume, loop diuretics such as furosemide may be used cautiously [3,4]. This is best done with monitoring of:
- Weight change
- Urine output
- Blood pressure
- Serum sodium and potassium
- Serum creatinine

Intravenous albumin is a selective rather than routine intervention [3-6]. IPNA recommends that in severe edema, 20% or 25% albumin 0.5-1 g/kg over 4-6 hours may be given with intravenous furosemide 1-2 mg/kg during the middle and/or at the end of the infusion, provided there is not marked intravascular contraction and/or hyponatremia [3]. The rationale is physiologic: albumin may transiently increase effective circulating volume and restore diuretic responsiveness in selected patients [3,4]. However, the direct evidence base is thin. The Cochrane review found only one small pediatric randomized trial, and the 2025 pediatric systematic review similarly concluded that evidence for routine IV albumin use remains extremely limited and mostly supports only short-term physiologic benefits [5,6].

If true hypovolemia or hypovolemic shock is present, treat perfusion first rather than trying to force diuresis [3,4]. IPNA recommends acute volume resuscitation, typically with 4% or 5% albumin 20 mL/kg over 20-30 minutes, or isotonic saline if albumin is not available [3]. Once perfusion improves, reassess whether further edema-directed therapy is actually needed.

Edema usually improves most durably when the nephrotic state remits. Supportive maneuvers alone are rarely definitive [1-4].

### Harms / pitfalls
The main pitfall is treating all edema as hypervolemia. Diuretics in a hypovolemic child can worsen AKI and thrombosis risk and may intensify shock physiology [3,4]. Albumin infusion can also cause harm, including hypertension, pulmonary edema, or fluid overload, especially when urine output is poor or intravascular volume is already expanded [3-6].

Other common pitfalls include:
- Ordering routine fluid restriction despite guideline advice against it for most cases [3]
- Escalating albumin or furosemide repeatedly without re-checking volume status and kidney function [3,4]
- Mistaking pseudohyponatremia related to hyperlipidemia for a reason to intensify fluid restriction [3]
- Focusing on edema alone and missing infection, thrombosis, steroid resistance, or alternate causes of worsening swelling [1,3]

## What remains uncertain
The best candidates, timing, and outcome impact for albumin plus furosemide remain uncertain because pediatric comparative evidence is sparse [5,6]. There is also no single bedside test that perfectly separates underfill from overfill physiology in every child. Much of edema treatment therefore still depends on serial clinical reassessment informed by guideline-based caution rather than on strong randomized evidence.

## Practical takeaways for residents
- Ask first whether the child is intravascularly dry, adequately filled, or overloaded before ordering diuretics or albumin [3,4].
- Use sodium restriction for active moderate to severe edema; do not default to routine fluid restriction [3].
- Avoid diuretics for uncomplicated edema and be especially cautious when oliguria, abdominal pain, rising creatinine, or low blood pressure suggests hypovolemia [3,4].
- Reserve albumin plus furosemide for selected severe cases, usually in monitored settings, and watch closely for pulmonary edema, hypertension, electrolyte shifts, and creatinine rise [3-6].
- If there is shock or clear poor perfusion, resuscitate first and reassess the edema plan afterward [3].
- Expect the most durable improvement to follow remission of proteinuria rather than supportive fluid maneuvers alone [1-4].

## Source map
1. Kidney Disease: Improving Global Outcomes (KDIGO) Nephrotic Syndrome in Children Work Group. KDIGO 2025 Clinical Practice Guideline for the Management of Nephrotic Syndrome in Children. Kidney Int. 2025;107(5 Suppl):S241-S289. doi:10.1016/j.kint.2024.11.005. Available at: https://kdigo.org/wp-content/uploads/2025/04/KDIGO-2025-Guideline-for-Nephrotic-Syndrome-in-Children.pdf
2. Floege J, Gibson KL, Vivarelli M, et al. Executive summary of the KDIGO 2025 Clinical Practice Guideline for the Management of Nephrotic Syndrome in Children. Kidney Int. 2025;107(4):806-808. doi:10.1016/j.kint.2024.11.006. PMID: 40254362. Available at: https://kdigo.org/wp-content/uploads/2025/04/KDIGO-2025-Nephrotic-Syndrome-in-Children-Guideline-Executive-Summary.pdf
3. Trautmann A, Boyer O, Hodson E, et al. IPNA clinical practice recommendations for the diagnosis and management of children with steroid-sensitive nephrotic syndrome. Pediatr Nephrol. 2023;38(3):877-919. doi:10.1007/s00467-022-05739-3. PMID: 36269406. PMCID: PMC9589698. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC9589698/
4. Kallash M, Mahan JD. Mechanisms and management of edema in pediatric nephrotic syndrome. Pediatr Nephrol. 2021;36(7):1719-1730. doi:10.1007/s00467-020-04779-x. PMID: 33216218. Available at: https://pubmed.ncbi.nlm.nih.gov/33216218/
5. Ho JJ, Adnan AS, Kueh YC, Ambak NJ, Van Rostenberghe H, Jummaat F. Human albumin infusion for treating oedema in people with nephrotic syndrome. Cochrane Database Syst Rev. 2019;7(7):CD009692. doi:10.1002/14651858.CD009692.pub2. PMID: 31425606. PMCID: PMC6699680. Available at: https://pubmed.ncbi.nlm.nih.gov/31425606/
6. Nawaz SB, Zafar MA. Intravenous Albumin for Oedema in Children With Nephrotic Syndrome: A Systematic Review and Mapping of the Evidence Landscape. Cureus. 2025;17(10):e95142. doi:10.7759/cureus.95142. PMID: 41281089. PMCID: PMC12636047. Available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC12636047/

## Caveats
This is a focused evidence note, not a formal systematic review. Most direct edema-treatment recommendations in children are driven by guideline consensus and pathophysiology-informed reasoning rather than large pediatric randomized trials [3-6]. The strongest edema-specific guidance comes from idiopathic and steroid-sensitive childhood nephrotic syndrome literature, so extrapolation to secondary nephrotic syndromes or steroid-resistant disease should be cautious. The evidence for albumin-based therapy remains especially limited and mainly supports short-term physiologic effects rather than proven patient-centered benefits [5,6].

## Last updated
2026-04-19

```
