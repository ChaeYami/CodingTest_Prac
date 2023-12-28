from collections import Counter, defaultdict
from datetime import datetime
import os
import re

def count_problem_source_code():
    
    problem_solve_code_list = []

    directory_list = [directory for directory in os.listdir("./") if "2023" in directory or "2024" in directory]

    file_count_by_month_year = defaultdict(int)
    
    for directory in directory_list:
        code_list = os.listdir(f"./{directory}")
        
        # 사이트별
        problem_solve_code_list += code_list
        
        
        #날짜별
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                creation_date = datetime.utcfromtimestamp(os.path.getctime(file_path))

                month_year_key = creation_date.strftime("%m-%Y")

                file_count_by_month_year[month_year_key] += 1

    # 사이트별
    name_list = [re.findall(r'\[[^)]*\]', code_name) for code_name in problem_solve_code_list]

    name_list = [name[0].replace("[", "").replace("]", "") for name in name_list if len(name) > 0]

    total_code_num = len(name_list)
    
    code_cnt_info = sorted(Counter(name_list).items(), key=lambda x: -x[1])
    
    
    # 날짜별
    month_files_info = sorted(file_count_by_month_year.items(), key=lambda x: (int(x[0][3:]), int(x[0][:2])))
    
    return total_code_num, code_cnt_info, month_files_info


def make_count_site_info(total_code_num, code_cnt_info):
    count_info = f"## 해결한 문제 : {total_code_num}개\n"

    for name in code_cnt_info:
        temp = f"#### {name[0]} - {name[1]}개\n"
        count_info += temp

    return count_info

def make_count_month_info(month_files_info):
    month_info = f"### 날짜별 해결한 문제 \n"
    
    for month_year, count in month_files_info:
        formatted_month_year = datetime.strptime(month_year, "%m-%Y").strftime("%b-%Y")
        
        temp = f"#### {formatted_month_year} : {count}개\n"
        month_info += temp
        
    return month_info


def make_read_me(count_info, month_info):
    return f"""# ⭐ 코딩테스트 연습 ( CODINGTEST PRACTICE ) ⭐
{count_info}
{month_info}
"""

def update_readme_md():
    total_code_num, code_cnt_info, month_files_info = count_problem_source_code()
    count_info = make_count_site_info(total_code_num=total_code_num, code_cnt_info=code_cnt_info)

    month_info = make_count_month_info(month_files_info=month_files_info)
    
    readme = make_read_me(count_info=count_info, month_info=month_info)

    return readme


if __name__ == "__main__":
    readme = update_readme_md()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)

