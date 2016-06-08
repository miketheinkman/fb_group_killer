# fb_group_killer
If you admin a group, and you are sick of it, run this to ban every member

## Graph API sucks. You can only admin a group with the API if the API app Created the group.

The UI is also a little tricky to scrape and interact with through scripting. This script will ban all members of a group, at the rate of about 10 seconds per ban.

## Directions

1 Copy this script to your computer

2 Make sure you have Python 2.x

3 pip install selenium

4 firefox version compatible with selenium

5 fill out variables at top of script. email, password, number of admins, and the url for the members page of your group example: https://www.facebook.com/groups/your group number/members/

6 run the script

It should take about 6 days to ban 50,000 people from a group. I will confirm this soon, as I am about to nuke 50,000 people out of a group I admin. I suppose you could run multiple instances to speed it along, but I'm not going to bother.
