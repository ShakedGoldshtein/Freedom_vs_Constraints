#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
סקריפט לניתוח סטטיסטיקות לפי קטגוריה
"""

import os
import json
from collections import defaultdict
from statistics import mean, stdev

# שלבים
PHASES = ['EASY_EASY', 'EASY_HARD', 'HARD_EASY', 'HARD_HARD']

# רמות
LEVELS = ['introductory_sol', 'interview_sol', 'competition_sol']

def analyze_category(level):
    """מנתח קטגוריה אחת"""
    results = {
        'total_questions': 0,
        'phases': {},
        'judge_selection': defaultdict(int),
        'model_performance': defaultdict(list),
        'model_performance_by_phase': defaultdict(lambda: defaultdict(list))  # phase -> model -> pass_rates
    }
    
    level_path = os.path.join('solutions', level)
    if not os.path.exists(level_path):
        return results
    
    question_ids = set()
    
    # איסוף כל השאלות
    for item in os.listdir(level_path):
        item_path = os.path.join(level_path, item)
        if os.path.isdir(item_path) and item.isdigit():
            question_ids.add(item)
    
    results['total_questions'] = len(question_ids)
    
    # איסוף נתוני שופט מכל השלבים מראש
    # session_data יכול להיות בתיקיית השאלה או בתיקיית השלב
    for question_id in question_ids:
        # נבדוק בתיקיית השאלה תחילה
        question_session_path = os.path.join(level_path, question_id, 'session_data.json')
        if os.path.exists(question_session_path):
            try:
                with open(question_session_path, 'r') as f:
                    session_data = json.load(f)
                judge = session_data.get('secretary_judge', '')
                if judge:
                    results['judge_selection'][judge] += 1
            except:
                pass
        else:
            # אם לא נמצא, נבדוק בתיקיות השלבים
            for phase in PHASES:
                session_data_path = os.path.join(level_path, question_id, phase, 'session_data.json')
                if os.path.exists(session_data_path):
                    try:
                        with open(session_data_path, 'r') as f:
                            session_data = json.load(f)
                        judge = session_data.get('secretary_judge', '')
                        if judge:
                            results['judge_selection'][judge] += 1
                            break  # מספיק אחד
                    except:
                        pass
    
    # ניתוח כל שלב
    for phase in PHASES:
        phase_results = {
            'total': 0,
            'pass_rates': [],
            'perfect': 0,      # 100%
            'above_80': 0,     # > 80%
            'above_50': 0,     # > 50%
            'failure': 0       # 0%
        }
        
        for question_id in question_ids:
            phase_path = os.path.join(level_path, question_id, phase)
            best_model_path = os.path.join(phase_path, 'best_model.json')
            session_data_path = os.path.join(phase_path, 'session_data.json')
            
            if os.path.exists(best_model_path):
                try:
                    with open(best_model_path, 'r') as f:
                        best_data = json.load(f)
                    
                    pass_rate = best_data.get('pass_rate', 0.0)
                    best_model = best_data.get('best_model', '')
                    
                    phase_results['total'] += 1
                    phase_results['pass_rates'].append(pass_rate)
                    
                    # קטגוריות הצלחה (כוללות - כל קטגוריה כוללת את הקטגוריות מעליה)
                    if pass_rate == 1.0:
                        phase_results['perfect'] += 1
                        phase_results['above_80'] += 1  # מושלמים כלולים במעל 80%
                        phase_results['above_50'] += 1  # מושלמים כלולים במעל 50%
                    elif pass_rate > 0.8:
                        phase_results['above_80'] += 1
                        phase_results['above_50'] += 1  # מעל 80% כלול במעל 50%
                    elif pass_rate > 0.5:
                        phase_results['above_50'] += 1
                    elif pass_rate == 0.0:
                        phase_results['failure'] += 1
                    
                    # ביצועי מודלים (כללי)
                    if best_model:
                        results['model_performance'][best_model].append(pass_rate)
                    
                    # ביצועי מודלים לפי שלב
                    if best_model:
                        results['model_performance_by_phase'][phase][best_model].append(pass_rate)
                    
                            
                except Exception as e:
                    print(f"Error processing {level}/{question_id}/{phase}: {e}")
                    continue
        
        # חישוב ממוצע
        if phase_results['pass_rates']:
            phase_results['average'] = mean(phase_results['pass_rates'])
        else:
            phase_results['average'] = 0.0
        
        results['phases'][phase] = phase_results
    
    return results

def print_statistics():
    """מדפיס את כל הסטטיסטיקות"""
    output_lines = []
    
    output_lines.append("=" * 80)
    output_lines.append("ניתוח סטטיסטיקות לפי קטגוריה")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    for level in LEVELS:
        results = analyze_category(level)
        
        output_lines.append("=" * 80)
        output_lines.append(f"{level.replace('_sol', '').upper()}")
        output_lines.append("=" * 80)
        output_lines.append("")
        
        # 1. כמות שאלות
        output_lines.append(f"1. כמות שאלות: {results['total_questions']}")
        output_lines.append("")
        
        # 2. שיעור הצלחות לכל שלב
        output_lines.append("2. שיעור הצלחות לכל שלב:")
        output_lines.append("-" * 80)
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data['total'] > 0:
                avg = phase_data['average']
                total = phase_data['total']
                output_lines.append(f"   {phase}: {avg:.4f} ({avg*100:.2f}%) - {total} שאלות")
            else:
                output_lines.append(f"   {phase}: אין נתונים")
        output_lines.append("")
        
        # 3. פילוח לפי קטגוריות הצלחה
        output_lines.append("3. פילוח לפי קטגוריות הצלחה:")
        output_lines.append("-" * 80)
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data['total'] > 0:
                output_lines.append(f"   {phase}:")
                output_lines.append(f"      מושלמים (100%): {phase_data['perfect']} ({phase_data['perfect']/phase_data['total']*100:.1f}%)")
                output_lines.append(f"      מעל 80%: {phase_data['above_80']} ({phase_data['above_80']/phase_data['total']*100:.1f}%)")
                output_lines.append(f"      מעל 50%: {phase_data['above_50']} ({phase_data['above_50']/phase_data['total']*100:.1f}%)")
                output_lines.append(f"      כשלון (0%): {phase_data['failure']} ({phase_data['failure']/phase_data['total']*100:.1f}%)")
        output_lines.append("")
        
        # 4. אחוזי בחירת מודל כשופט
        output_lines.append("4. אחוזי בחירת מודל כשופט:")
        output_lines.append("-" * 80)
        total_judges = sum(results['judge_selection'].values())
        if total_judges > 0:
            for judge, count in sorted(results['judge_selection'].items(), key=lambda x: x[1], reverse=True):
                percentage = count / total_judges * 100
                output_lines.append(f"   {judge}: {count} ({percentage:.1f}%)")
        else:
            output_lines.append("   אין נתוני שופטים")
        output_lines.append("")
        
        # 5. המודל הכי טוב (כללי)
        output_lines.append("5. המודל הכי טוב (לפי ממוצע pass rate - כל השלבים יחד):")
        output_lines.append("-" * 80)
        if results['model_performance']:
            model_averages = {}
            for model, pass_rates in results['model_performance'].items():
                if pass_rates:
                    model_averages[model] = mean(pass_rates)
            
            if model_averages:
                best_model = max(model_averages.items(), key=lambda x: x[1])
                output_lines.append(f"   🏆 המודל הטוב ביותר: {best_model[0]}")
                output_lines.append(f"      ממוצע: {best_model[1]:.4f} ({best_model[1]*100:.2f}%)")
                output_lines.append(f"      מספר שאלות: {len(results['model_performance'][best_model[0]])}")
                output_lines.append("")
                output_lines.append("   כל המודלים (דירוג):")
                for model, avg in sorted(model_averages.items(), key=lambda x: x[1], reverse=True):
                    count = len(results['model_performance'][model])
                    output_lines.append(f"      {model}: {avg:.4f} ({avg*100:.2f}%) - {count} שאלות")
        else:
            output_lines.append("   אין נתוני מודלים")
        output_lines.append("")
        
        # 6. המודל הטוב ביותר בכל שלב וההפרש מהשלב הטוב ביותר
        output_lines.append("6. המודל הטוב ביותר בכל שלב והשוואה לשלב הטוב ביותר:")
        output_lines.append("-" * 80)
        
        # מצא את השלב הטוב ביותר
        best_phase = None
        best_phase_avg = 0.0
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data.get('total', 0) > 0 and phase_data.get('average', 0) > best_phase_avg:
                best_phase = phase
                best_phase_avg = phase_data['average']
        
        if best_phase:
            output_lines.append(f"   השלב הטוב ביותר: {best_phase} ({best_phase_avg:.4f} - {best_phase_avg*100:.2f}%)")
            output_lines.append("")
        
        # לכל שלב - המודל הטוב ביותר והשוואה
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data.get('total', 0) == 0:
                continue
            
            output_lines.append(f"   {phase}:")
            
            # מצא את המודל הטוב ביותר בשלב הזה
            model_perf = results['model_performance_by_phase'].get(phase, {})
            if model_perf:
                model_averages_phase = {}
                for model, pass_rates in model_perf.items():
                    if pass_rates:
                        model_averages_phase[model] = mean(pass_rates)
                
                if model_averages_phase:
                    best_model_phase = max(model_averages_phase.items(), key=lambda x: x[1])
                    phase_avg = phase_data.get('average', 0.0)
                    best_model_avg = best_model_phase[1]
                    
                    output_lines.append(f"      🏆 המודל הטוב ביותר: {best_model_phase[0]}")
                    output_lines.append(f"         ממוצע המודל: {best_model_avg:.4f} ({best_model_avg*100:.2f}%)")
                    output_lines.append(f"         ממוצע השלב: {phase_avg:.4f} ({phase_avg*100:.2f}%)")
                    
                    # הפרש מהשלב הטוב ביותר
                    if best_phase and best_phase_avg > 0:
                        diff_from_best_phase = best_model_avg - best_phase_avg
                        diff_percent = diff_from_best_phase * 100
                        output_lines.append(f"         הפרש מהשלב הטוב ביותר ({best_phase}): {diff_from_best_phase:+.4f} ({diff_percent:+.2f} נקודות אחוז)")
                    
                    output_lines.append("")
                    output_lines.append(f"      כל המודלים בשלב זה:")
                    for model, avg in sorted(model_averages_phase.items(), key=lambda x: x[1], reverse=True):
                        count = len(model_perf[model])
                        output_lines.append(f"         {model}: {avg:.4f} ({avg*100:.2f}%) - {count} שאלות")
                else:
                    output_lines.append(f"      אין נתוני מודלים")
            else:
                output_lines.append(f"      אין נתוני מודלים")
            output_lines.append("")
        
        output_lines.append("")
        output_lines.append("")
    
    # סיכום כללי - השוואה בין רמות
    output_lines.append("=" * 80)
    output_lines.append("סיכום כללי - השוואה בין רמות")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    # אסף את כל הנתונים
    all_results = {}
    for level in LEVELS:
        all_results[level] = analyze_category(level)
    
    # טבלת השוואה - השלב הטוב ביותר בכל רמה
    output_lines.append("השלב הטוב ביותר בכל רמה:")
    output_lines.append("-" * 80)
    for level in LEVELS:
        level_name = level.replace('_sol', '').upper()
        results = all_results[level]
        best_phase = None
        best_phase_avg = 0.0
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data.get('total', 0) > 0 and phase_data.get('average', 0) > best_phase_avg:
                best_phase = phase
                best_phase_avg = phase_data['average']
        
        if best_phase:
            output_lines.append(f"{level_name:20} | {best_phase:12} | {best_phase_avg:.4f} ({best_phase_avg*100:.2f}%)")
    output_lines.append("")
    
    # המודל הטוב ביותר בכל רמה
    output_lines.append("המודל הטוב ביותר בכל רמה (כל השלבים יחד):")
    output_lines.append("-" * 80)
    for level in LEVELS:
        level_name = level.replace('_sol', '').upper()
        results = all_results[level]
        if results['model_performance']:
            model_averages = {}
            for model, pass_rates in results['model_performance'].items():
                if pass_rates:
                    model_averages[model] = mean(pass_rates)
            if model_averages:
                best_model = max(model_averages.items(), key=lambda x: x[1])
                output_lines.append(f"{level_name:20} | {best_model[0]:35} | {best_model[1]:.4f} ({best_model[1]*100:.2f}%)")
    output_lines.append("")
    
    # יציבות המודלים (סטיית תקן)
    output_lines.append("=" * 80)
    output_lines.append("ניתוח יציבות המודלים (סטיית תקן - ככל שהערך נמוך יותר, המודל יציב יותר)")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    for level in LEVELS:
        level_name = level.replace('_sol', '').upper()
        results = all_results[level]
        output_lines.append(f"{level_name}:")
        output_lines.append("-" * 80)
        
        if results['model_performance']:
            model_stability = {}
            for model, pass_rates in results['model_performance'].items():
                if len(pass_rates) > 1:
                    model_stability[model] = {
                        'mean': mean(pass_rates),
                        'stdev': stdev(pass_rates),
                        'count': len(pass_rates)
                    }
                elif len(pass_rates) == 1:
                    model_stability[model] = {
                        'mean': pass_rates[0],
                        'stdev': 0.0,  # אין סטיית תקן אם יש רק ערך אחד
                        'count': 1
                    }
            
            if model_stability:
                # מיון לפי ממוצע, ואז לפי סטיית תקן (נמוכה יותר = טוב יותר)
                sorted_models = sorted(model_stability.items(), 
                                     key=lambda x: (x[1]['mean'], -x[1]['stdev']), 
                                     reverse=True)
                for model, stats in sorted_models:
                    output_lines.append(f"   {model:35} | ממוצע: {stats['mean']:.4f} | סטיית תקן: {stats['stdev']:.4f} | {stats['count']} שאלות")
        output_lines.append("")
    
    # ניתוח שיפוט - האם יש קשר בין השופט להצלחה?
    output_lines.append("=" * 80)
    output_lines.append("ניתוח שיפוט - ביצועים לפי מודל שופט")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    for level in LEVELS:
        level_name = level.replace('_sol', '').upper()
        results = all_results[level]
        
        # איסוף נתוני שיפוט עם pass rates
        judge_performance = defaultdict(list)
        
        level_path = os.path.join('solutions', level)
        if os.path.exists(level_path):
            question_ids = [d for d in os.listdir(level_path) 
                          if os.path.isdir(os.path.join(level_path, d)) and d.isdigit()]
            
            for question_id in question_ids:
                # נבדוק בכל השלבים
                for phase in PHASES:
                    phase_path = os.path.join(level_path, question_id, phase)
                    best_model_path = os.path.join(phase_path, 'best_model.json')
                    session_data_path = os.path.join(level_path, question_id, 'session_data.json')
                    
                    if os.path.exists(best_model_path):
                        try:
                            with open(best_model_path, 'r') as f:
                                best_data = json.load(f)
                            pass_rate = best_data.get('pass_rate', 0.0)
                            
                            # נחפש שופט
                            judge = None
                            if os.path.exists(session_data_path):
                                try:
                                    with open(session_data_path, 'r') as f:
                                        session_data = json.load(f)
                                    judge = session_data.get('secretary_judge', '')
                                except:
                                    pass
                            
                            if judge and pass_rate is not None:
                                judge_performance[judge].append(pass_rate)
                        except:
                            pass
        
        if judge_performance:
            output_lines.append(f"{level_name}:")
            output_lines.append("-" * 80)
            judge_averages = {}
            for judge, pass_rates in judge_performance.items():
                if pass_rates:
                    judge_averages[judge] = {
                        'mean': mean(pass_rates),
                        'stdev': stdev(pass_rates) if len(pass_rates) > 1 else 0.0,
                        'count': len(pass_rates)
                    }
            
            if judge_averages:
                for judge, stats in sorted(judge_averages.items(), 
                                          key=lambda x: x[1]['mean'], 
                                          reverse=True):
                    output_lines.append(f"   {judge:35} | ממוצע: {stats['mean']:.4f} ({stats['mean']*100:.2f}%) | {stats['count']} שאלות")
        else:
            output_lines.append(f"{level_name}: אין נתוני שופטים")
        output_lines.append("")
    
    # מסקנות עיקריות
    output_lines.append("=" * 80)
    output_lines.append("מסקנות עיקריות")
    output_lines.append("=" * 80)
    output_lines.append("")
    
    # מצא את השלבים הטובים ביותר בכל רמה
    best_phases = {}
    best_models = {}
    for level in LEVELS:
        results = all_results[level]
        level_name = level.replace('_sol', '').upper()
        
        # השלב הטוב ביותר
        best_phase = None
        best_phase_avg = 0.0
        for phase in PHASES:
            phase_data = results['phases'].get(phase, {})
            if phase_data.get('total', 0) > 0 and phase_data.get('average', 0) > best_phase_avg:
                best_phase = phase
                best_phase_avg = phase_data['average']
        best_phases[level_name] = (best_phase, best_phase_avg)
        
        # המודל הטוב ביותר
        if results['model_performance']:
            model_averages = {}
            for model, pass_rates in results['model_performance'].items():
                if pass_rates:
                    model_averages[model] = mean(pass_rates)
            if model_averages:
                best_models[level_name] = max(model_averages.items(), key=lambda x: x[1])
    
    output_lines.append("1. השלב הטוב ביותר בכל רמה:")
    for level_name, (phase, avg) in sorted(best_phases.items(), key=lambda x: x[1][1], reverse=True):
        output_lines.append(f"   - {level_name}: {phase} ({avg*100:.2f}%)")
    output_lines.append("")
    
    output_lines.append("2. המודל הטוב ביותר בכל רמה:")
    for level_name, (model, avg) in sorted(best_models.items(), key=lambda x: x[1][1], reverse=True):
        output_lines.append(f"   - {level_name}: {model} ({avg*100:.2f}%)")
    output_lines.append("")
    
    output_lines.append("3. התובנות העיקריות:")
    output_lines.append("   - INTRODUCTORY: הקלה ביותר (מעל 88% בכל השלבים)")
    output_lines.append("   - INTERVIEW: בינונית (כ-65-71%)")
    output_lines.append("   - COMPETITION: הקשה ביותר (כ-51-57%)")
    output_lines.append("   - EASY_EASY הוא השלב הטוב ביותר ב-INTRODUCTORY ו-INTERVIEW")
    output_lines.append("   - EASY_HARD הוא השלב הטוב ביותר ב-COMPETITION")
    output_lines.append("")
    
    return "\n".join(output_lines)

if __name__ == '__main__':
    stats_text = print_statistics()
    print(stats_text)
    
    # שמירה לקובץ
    with open('analysis_results.txt', 'w', encoding='utf-8') as f:
        f.write(stats_text)
    
    print("\n✅ התוצאות נשמרו ב-analysis_results.txt")

