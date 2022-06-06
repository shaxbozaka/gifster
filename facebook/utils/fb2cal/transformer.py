

class Transformer:

    def transform_birthday_comet_monthly_to_birthdays(self, birthday_comet_root_json):
        """ Transforms outfrom from BirthdayCometMonthlyBirthdaysRefetchQuery to list of Birthdays """

        facebook_users = []

        for all_friends_by_birthday_month_edge in birthday_comet_root_json['data']['viewer']['all_friends_by_birthday_month']['edges']:
            for friend_edge in all_friends_by_birthday_month_edge['node']['friends']['edges']:
                friend = friend_edge['node']
                
                # Create Birthday object
                facebook_users.append(
                    {
                        "id": friend["id"],
                        "name": friend["name"],
                        "profile_url": friend["profile_url"],
                        "profile_picture": friend["profile_picture"]["uri"],
                        "birth_day": friend["birthdate"]["day"],
                        "birth_month": friend["birthdate"]["month"],
                        "birthdate_year": friend["birthdate"]["year"]
                    })
                
        return facebook_users