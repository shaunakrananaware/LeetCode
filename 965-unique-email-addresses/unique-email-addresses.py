class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = {}
        unique_email_count = 0

        for idx in range(len(emails)):
            local_email = ''
            
            jdx = 0
            while emails[idx][jdx] != '@':
                if emails[idx][jdx] == '+':
                    while emails[idx][jdx] != '@':
                        jdx += 1
                    break

                if emails[idx][jdx] == '.':
                    jdx += 1
                    continue

                local_email += emails[idx][jdx]
                jdx += 1
            
            final_email = f'{local_email}{emails[idx][jdx:]}'
            
            if final_email not in unique_emails: 
                unique_emails[final_email] = 0
                unique_email_count += 1
        
        return unique_email_count

