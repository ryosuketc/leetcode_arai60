class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def standardize_local_name(local_name):
            standardized_local_name = []
            for c in local_name:
                if c == '.':
                    continue
                if c == '+':
                    break
                standardized_local_name.append(c)
            return ''.join(standardized_local_name)

        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            standardized_local_name = standardize_local_name(local_name)
            standardized_email = '@'.join([standardized_local_name, domain_name])
            unique_emails.add(standardized_email)

        return len(unique_emails)
