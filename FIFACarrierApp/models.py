from django.db import models

class PLayersData(models.Model):
    sofi_id = models.IntegerField(blank="False")
    player_url = models.CharField(max_length=250, blank="True")
    short_name = models.CharField(max_length=100)
    long_name = models.CharField(max_length=200)
    player_position = models.CharField(max_length=30)
    overall = models.IntegerField(blank="False")
    potential = models.IntegerField(blank="False")
    value_eur = models.IntegerField(blank="False")
    wage_eur = models.IntegerField(blank="False")
    age = models.IntegerField(blank="False")
    dob = models.CharField(max_length=100)
    height_cm = models.IntegerField(blank="False")
    weight_kg = models.IntegerField(blank="False")
    club_team_id = models.IntegerField(blank="False")
    club_name = models.CharField(max_length=100)
    league_name = models.CharField(max_length=100)
    league_level = models.IntegerField(blank="False")
    club_position = models.CharField(max_length=20)
    club_jersey_number = models.IntegerField(blank="False")
    club_loaned_from = models.CharField(max_length=100, blank="True")
    club_joined = models.CharField(max_length=100)
    club_contract_valid_until = models.IntegerField(blank="False")
    nationality_id = models.IntegerField(blank="False")
    nationality_name = models.CharField(max_length=50)
    nation_team_id = models.IntegerField(blank="True", null="True")
    nation_position = models.CharField(max_length=20, blank="True")
    nation_jersey_number = models.IntegerField(blank="True", null="True")
    preferred_foot = models.CharField(max_length=10)
    weak_foot = models.IntegerField(blank="False")
    skill_moves = models.IntegerField(blank="False")
    national_reputation = models.IntegerField(blank="False")
    work_rate = models.CharField(max_length=30)
    body_type = models.CharField(max_length=30)
    real_face = models.CharField(max_length=10)
    release_clause_eur = models.IntegerField(blank="True", null="True")
    player_tags = models.CharField(max_length=200, blank="True")
    player_traits = models.CharField(max_length=300, blank="True")
    pace = models.IntegerField(blank="False")
    shooting = models.IntegerField(blank="False")
    passing = models.IntegerField(blank="False")
    dribbling = models.IntegerField(blank="False")
    defending = models.IntegerField(blank="False")
    physic = models.IntegerField(blank="False")
    attacking_crossing = models.IntegerField(blank="False")
    attacking_finishing = models.IntegerField(blank="False")
    attacking_heading_accuracy = models.IntegerField(blank="False")
    attacking_short_passing = models.IntegerField(blank="False")
    attacking_volleys = models.IntegerField(blank="False")
    skill_dribbling = models.IntegerField(blank="False")
    skill_curve = models.IntegerField(blank="False")
    skill_fk_accuracy = models.IntegerField(blank="False")
    skill_long_passing = models.IntegerField(blank="False")
    skill_ball_control = models.IntegerField(blank="False")
    movement_acceleration = models.IntegerField(blank="False")
    movement_sprint_speed = models.IntegerField(blank="False")
    movement_agility = models.IntegerField(blank="False")
    movement_reactions = models.IntegerField(blank="False")
    movement_balance = models.IntegerField(blank="False")
    power_shot_power = models.IntegerField(blank="False")
    power_jumping = models.IntegerField(blank="False")
    power_stamina = models.IntegerField(blank="False")
    power_strength = models.IntegerField(blank="False")
    power_long_shots = models.IntegerField(blank="False")
    mentality_aggression = models.IntegerField(blank="False")
    mentality_interceptions = models.IntegerField(blank="False")
    mentality_positioning = models.IntegerField(blank="False")
    mentality_vision = models.IntegerField(blank="False")
    mentality_penalties = models.IntegerField(blank="False")
    mentality_composure = models.IntegerField(blank="False")
    defending_marking_awarness = models.IntegerField(blank="False")
    defending_standing_tackle = models.IntegerField(blank="False")
    defending_sliding_tackle = models.IntegerField(blank="False")
    goalkeeping_diving = models.IntegerField(blank="False")
    goalkeeping_handling = models.IntegerField(blank="False")
    goalkeeping_kicking = models.IntegerField(blank="False")
    goalkeeping_positioning = models.IntegerField(blank="False")
    goalkeeping_reflexes = models.IntegerField(blank="False")
    goalkeeping_speed = models.IntegerField(blank="False")
    ls = models.CharField(max_length=10, blank="True")
    st = models.CharField(max_length=10, blank="True")
    rs = models.CharField(max_length=10, blank="True")
    lw = models.CharField(max_length=10, blank="True")
    lf = models.CharField(max_length=10, blank="True")
    cf = models.CharField(max_length=10, blank="True")  
    rf = models.CharField(max_length=10, blank="True")
    rw = models.CharField(max_length=10, blank="True")
    lam = models.CharField(max_length=10, blank="True")
    cam = models.CharField(max_length=10, blank="True")
    ram = models.CharField(max_length=10, blank="True")
    lm = models.CharField(max_length=10, blank="True")
    lcm = models.CharField(max_length=10, blank="True")
    cm = models.CharField(max_length=10, blank="True")
    rcm = models.CharField(max_length=10, blank="True")
    rm = models.CharField(max_length=10, blank="True")
    lwb = models.CharField(max_length=10, blank="True")
    ldm = models.CharField(max_length=10, blank="True")
    cdm = models.CharField(max_length=10, blank="True")
    rdm = models.CharField(max_length=10, blank="True")
    rwb = models.CharField(max_length=10, blank="True")
    lb = models.CharField(max_length=10, blank="True")
    lcb = models.CharField(max_length=10, blank="True")
    cb = models.CharField(max_length=10, blank="True")
    rcb = models.CharField(max_length=10, blank="True")
    rb = models.CharField(max_length=10, blank="True")
    gk = models.CharField(max_length=10, blank="True")
    player_face_url = models.CharField(max_length=200, blank="True")
    club_logo_url = models.CharField(max_length=200, blank="True")
    club_flag_url = models.CharField(max_length=200, blank="True")
    nation_logo_url = models.CharField(max_length=200, blank="True")
    nation_flag_url = models.CharField(max_length=200, blank="True")
    




