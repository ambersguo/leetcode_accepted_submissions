// https://leetcode.com/problems/unique-email-addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_new = []
        for email in emails:
            (local, domain) = email.split('@')
            if '.' in local:
                local = local.replace('.', '')
            if '+' in local:
                eles = local.split('+')
                local = eles[0]
            email_new = local + '@' + domain
            emails_new.append(email_new)
        emails_set = set(emails_new)
        return len(emails_set)
