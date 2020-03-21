#Random Ghost generator version 1.0
import random

#==========================================DEFINITIONS=================
#Define the limits based on Ghost Rank
Limits = [
    [3,1,4,1,1],
    [5,5,8,1,3],
    [7,9,14,3,5],
    [9,15,25,5,7],
    [12,26,35,7,9],
    [15,36,45,9,11]
    ]
#Limits = [GhostRank[TraitLimit,AttMin,AttMax,NumMin,NumMax]]
#So Limits[3][0] is the Attribute Limit of a Rank 3 ghost.

#Initialize some variables that will be used later.
NuminaKnown = []
Numina = Numina = ["Anchor Jump", "Awe","Blast","Drain","Emotional aura","Firestarter","Hallucination","Host Jump", "Implant Mission", "Innocuous","Left-Handed Spanner","Moliate","Omen Trance","Pathfinder","Proxy","Puppeteer","Rapture","Regenerate","Seek","Speed","Sign","Stalwart","Telekinesis"]
Power = 1
Finesse = 1
Resistance = 1
Manifestations = ["Avernian Gateway", "Discorporate","Fetter","Image","Poessess","Unfetter"]
#^ Contains all Manifestations with no requirements, those get added conditionally to the list later
#That also doesn't contain Twilight Form, because everyone gets that so it's added for free at the end
ManifestationsKnown = []
Bans = [
    "This ghost lacks bans",
    "This ghost has an easy to trigger ban, but one that isn't dangerous",
    "This ghost should have a ban that seriously dirupts it",
    "This ghost should have a ban that seriously disrupts it",
    "This ghost should have a ban that truly foils the ghost in a dramatic way, but is esoteric and difficult to discover/pull off"
    ]
Banes = [
    "This ghost has an extremely common bane",
    "This ghost has a somewhat common bane - something you could find in an average household, but not necessarily in every room",
    "This ghost has a somewhat more rare bane, but it's still something natural - a particular wood or metal, or maybe a certain kind of animal. They never need to be specifically made.",
    "This ghost has a somewhat more rare bane, but it's still something natural - a particular wood or metal, or maybe a certain kind of animal. They never need to be specifically made.",
    "This ghost has a very specific bane that requires a large amount of effort to find or make."]

#==========================================MAIN BODY===================
#Ask for user input on 
GPick = input("What rank do you want your Ghost to be?  Enter a number, or a K if this is a ghost for a Krewe!\n >")
if (GPick != ('k' or 'K')) & (int(GPick) in range(0,5)):
    GRank = int(GPick)
    Manifestations.append("Materialize")#Krewe ghosts shouldn't have this, so it's only for non-K
elif GPick == ('k' or 'K'):
    GRank = 2
else:
    print("Please enter a number between 0 and 5, or the letter K to create a Krewe ghost!\nPlease re-run this script.")
    exit()
print("Hold please, conducting a seance...\n")

AttLim = Limits[GRank][0] #Make a nice handle for reference to max Atts
if GPick == ('k' or 'K'):
    AttPoints = 9
else:
    AttPoints = random.choice(range(Limits[GRank][1],Limits[GRank][2])) #Ghosts have a range of possible attributes to distribute based on rank.
if GPick == ('k' or 'K'):
    ManiPicks = 1
else:
    ManiPicks = GRank

#Determine how many numina our ghost gets.
if GPick == ('k' or 'K'):
    TotalNumina = 3
elif GRank == 0: #Border case - random didn't like a range function with a range of 1-1.
    TotalNumina = 1
else:
    TotalNumina = random.choice(range(Limits[GRank][3],Limits[GRank][4]))

print("==============================================")
print("STAT BLOCK: \n")
if GRank >= 3: #Add the Rank 3 requiring Numina and Manis
    Numina = Numina + ["Descend (Numina)", "Engulf"]
    Manifestations = Manifestations + ["Bargain"]

if GRank >= 2: #At Rank 2+, a Ghost can swap a Numina for another Mani, so they are in the same pool basically
    Numina = Numina + Manifestations

#Randomly select attributes
while AttPoints > 0:
    Bump = random.choice(["Pow","Fin","Res"])
    if (Bump == "Pow") & (Power <  AttLim):
        Power = Power + 1
        AttPoints = AttPoints - 1
    elif (Bump == "Fin") & (Finesse < AttLim):
        Finesse = Finesse + 1
        AttPoints = AttPoints - 1
    elif (Bump == "Res") & (Finesse < AttLim):
        Resistance = Resistance + 1
        AttPoints = AttPoints - 1
print("Power:" + str(Power) + "\nFinesse:" + str(Finesse) + "\nResistance:" + str(Resistance)+ "\n")

#Randomly select the Numina
while TotalNumina > 0:
    NuminaPick = random.choice(Numina)
    if NuminaPick not in NuminaKnown:
        NuminaKnown.append(NuminaPick)
        TotalNumina = TotalNumina - 1
print("Numen: \n" + str(NuminaKnown))

#Randomly select Manifestations
while ManiPicks > 0:
    ManiPick = random.choice(Manifestations)
    if (ManiPick not in ManifestationsKnown) & (ManiPick not in NuminaKnown):
        ManifestationsKnown.append(ManiPick)
        ManiPicks = ManiPicks - 1
        if ["Fetter","Posesses"] in ManifestationsKnown: #Add Claim if you meet prereqs
            Manifestations.append("Claim")
        if "Avernian Gateway" in ManifestationsKnown: #Add Descend if you meet prereqs
            Manifestations.append("Descend (Manifestations)")
ManifestationsKnown.append("Twilight Form") #All ghosts know this one for free in addition to their other known Manifestations
print("Manifestations: \n" + str(ManifestationsKnown) + "\n")

#Print a quick message about Bans, Banes, Virtue, and Vice:
print("Bans: " + Bans[GRank])
print("Banes: " + Banes[GRank])
print("The ghost should have a Virtue and a Vice")
#A quick word on Influences:
if GPick == ('k' or 'K'):
    print("Influences: Influence (Anchors) 2")
if GPick == ('k' or 'K'):
    print("Aspirations: Two, one of which should be about how they feel about death around them or their death.")
print("Influences: " + str(GRank) + " dots of Influences.\n At least one should probably be in Influence(Anchors).")

#Print derived stats:
print("\n")
print("Corpus: " + str(Resistance + 5) + "(Assuming they are Size 5)")
if (Resistance + Finesse) > 10:
    print("Willpower: 10")
else:
    print("Willpower: " + str(Resistance + Finesse))
print("Initiative: " + str(Finesse + Resistance))
if Resistance <= Power:
    print("Defense: " + str(Resistance))
else:
    print("Defense: " + str(Power))
print("Speed: " + str(Power + Finesse + 5))
print("Size: 5 (probably!)")


