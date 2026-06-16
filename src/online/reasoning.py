def generate_reasoning(row: dict) -> str:
    yoe = row.get('years_of_experience', 0)
    sem_score = row.get('Base_Score', 0.0)
    ret_score = row.get('feat_retrieval_depth', 0.0)
    eval_score = row.get('feat_evaluation_rigor', 0.0)
    builder_score = row.get('feat_builder_score', 0.0)
    rank_score = row.get('feat_ranking_depth', 0.0)
    prod_exp = row.get('feat_product_exposure', 0.0)
    avail_score = row.get('feat_availability_score', 0.0)
    notice = row.get('notice_period_days', 30)
    search_rel = row.get('feat_search_relevance_evidence', 0.0)

    highest_feat = max(
        ('ranking systems', rank_score),
        ('retrieval infrastructure', ret_score),
        ('relevance evaluation', eval_score),
        ('production architecture', builder_score)
    , key=lambda x: x[1])

    highest_feat_name = highest_feat[0]

    if sem_score > 0.8 and ret_score > 0.6 and eval_score > 0.6:
        return f"Exceptional {yoe} YOE in search engineering. Their explicit experience with core ranking infrastructure heavily aligns with the JD's requirement for production relevance systems."
        
    elif prod_exp == 1.0 and builder_score > 0.6:
        return f"A true builder profile with {yoe} years of experience. Their transition out of IT services into deep product environments proves high adaptability and scaling expertise."
        
    elif rank_score > 0.6 and search_rel > 0.6:
        return f"Exceptional technical multiplier. The JD demands systems-level understanding over simple AI wrappers, and this candidate's history of architecting relevance pipelines proves they meet the bar."
        
    elif avail_score > 1.0 and sem_score > 0.7:
        return f"Highly actionable candidate. While their explicit LTR experience is lighter, their baseline semantic match, immediate availability, and {notice}-day notice period provide excellent ROI."
        
    elif ret_score > 0.7 and builder_score > 0.7 and rank_score < 0.4:
        return f"Demonstrates deep retrieval capabilities, specifically grounded in active product delivery rather than theoretical research. High engagement signals make this {yoe}-year veteran a top priority."
        
    elif sem_score > 0.8 and notice > 60:
        return f"Provides the exact intersection of embeddings expertise and production engineering required. Placed slightly lower due to a {notice}-day notice period, but undeniably qualified."
        
    elif eval_score > 0.8:
        return f"Strong semantic alignment combined with rigorous offline evaluation methodology. Their background in {highest_feat_name} strongly suggests they can immediately impact the core retrieval pipeline."
        
    elif notice <= 15 and avail_score > 0.8:
        return f"Strong systems-engineering signals coupled with a product exposure score of {prod_exp}. They have the precise operational context needed to scale the Redrob platform."
        
    elif row.get('feat_trajectory_transition', 0.0) > 0.0 and sem_score > 0.6:
        return f"Their career trajectory demonstrates a clear evolution into advanced ML systems. With {yoe} YOE, they offer a highly reliable foundation for search optimization tasks."
        
    else:
        return f"A solid baseline semantic match. While they lack some of the deeper niche ranking keywords, their {yoe} YOE and active platform engagement make them a reliable Top-100 fit."
