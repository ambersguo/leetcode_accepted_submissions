// https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_digit = []
        logs_new = []
        content_id2log = {}
        letter_contents = []
        letter_ids = []
        seen = []
        
        for log in logs:
            log_list = log.split(' ')
            log_id = log_list[0]
            log_content_str_space = ' '.join(log_list[1:])
            log_content_str = ''.join(log_list[1:])
            content_id = log_content_str_space + '&' + log_id
            if log_content_str.isdigit():
                logs_digit.append(log)
            elif log_content_str.isalpha():
                content_id2log[content_id] = log
                letter_contents.append(log_content_str_space)
                letter_ids.append(log_id)
        
        letter_contents_uniq = list(set(letter_contents))
        letter_contents_uniq.sort()
        letter_ids.sort()

        for content in letter_contents_uniq:
            for log_id in letter_ids:
                content_id = content + '&' + log_id
                if content_id in content_id2log.keys():
                    if content_id not in seen:
                        logs_new.append(content_id2log[content_id])
                    seen.append(content_id)

        for log in logs_digit:
            logs_new.append(log)

        return logs_new
