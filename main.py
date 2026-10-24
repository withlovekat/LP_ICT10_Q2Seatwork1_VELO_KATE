

from pyscript import document 

def candidate_checker(e):
    club_members=["kate velo", "beatrice laus", "sakai moka"]
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + ' ' + l_name

    member_checker = candidate.lower() in club_members
    messages= (f'Sorry {candidate}, your name is not on the list.',
               f'Congratulations {candidate}! you are now part of the cutie patootie club !')

    document.getElementById('result').innerHTML = messages [int(member_checker)]