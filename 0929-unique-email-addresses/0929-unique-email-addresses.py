class Solution(object):
    def numUniqueEmails(self, emails):

        unique_emails = set()

        for email in emails:

            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')

            fixed_email = local + '@' + domain

            unique_emails.add(fixed_email)

        return len(unique_emails)    


        