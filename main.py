import asyncio
import interactions
from interactions.models.internal.context import SlashContext
from interactions import SlashContext, OptionType, slash_option
import discord
import random
from interactions import Client, Intents
from interactions.ext import prefixed_commands
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive

keep_alive()
bot = interactions.Client(token="MTE2NTg4MjI2OTkwMzM3MjMxOQ.GAJz82.QB-wXCAEDtuXJsdEeMeDB1bbrV_GckrgLHXw54")
robot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# Study commands
@bot.event()
async def on_ready():
    print("Teehee")
disease_lab = {
  "Bacillus Cereus": "**Illness**: B. cereus food poisoning. **Incubation** 10-16 hrs. **Symptoms**: Abdominal cramps, watery diarrhea, nausea. **Duration**: 24-48 hours. Source: Meats, stews, gravies, vanilla sauce ",
  "Campylobacter Jejuni" : "**Illness**: Campylobacteriosis. **Incubation** 2-5 days. **Symptoms**: Diarrhea, cramps, fever, and vomiting; diarrhea may be bloody. **Duration**: 2-10 days. Source: Raw and undercooked poultry, unpasteurized milk, contaminated water",
  "Clostridium Botulinum" : "**Illness**: Botulism. **Incubation** 12-72 hours. **Symptoms**: Vomiting, diarrhea, blurred vision, double vision, difficulty in swallowing, muscle weakness. Can result in respiratory failure and death. **Duration**: Variable. **Sources**: Improperly canned foods, especially home-canned vegetables, fermented fish, baked potatoes in aluminum foil",
  "Clostridium Perfringens" : "**Illness**: Perfringens food poisoning **Incubation**: 8–16 hours **Symptoms**: Intense abdominal cramps, watery diarrhea **Duration**: Usually 24 hours **Sources**: Meats, poultry, gravy, dried or precooked foods, time and/or temperature-abused foods",
  "Cryptosporidium" : "**Illness**: Intestinal cryptosporidiosis **Duration**: 2-10 days **Symptoms**: Diarrhea (usually watery), stomach cramps, upset stomach, slight fever **Duration**: May be remitting and relapsing over weeks to months **Sources**: Uncooked food or food contaminated by an ill food handler after cooking, contaminated drinking water",
  "Cyclospora Cayetanensis" : "**Illness**: Cyclosporiasis **Incubation**: 1-14 days, usually at least 1 week **Symptoms**: Diarrhea (usually watery), loss of appetite, substantial loss of weight, stomach cramps, nausea, vomiting, fatigue  **Duration**: May be remitting and relapsing over weeks to months **Sources**: Various types of fresh produce (imported berries, lettuce, basil)",
  "E.coli producing toxin" : "**Illness**: E. coli infection (common cause of “travelers’ diarrhea”) **Incubation**: 1-3 days **Symptoms**: Watery diarrhea, abdominal cramps, some vomiting **Duration**: 3-7 or more days **Sources**: Water or food contaminated with human feces",
  "E.coli O157:H7" : "**Illness**: Hemorrhagic colitis or E. coli O157:H7 infection **Incubation**: 1-8 days **Symptoms**: Severe (often bloody) diarrhea, abdominal pain and vomiting. Usually, little or no fever is present. More common in children 4 years or younger. Can lead to kidney failure **Duration**: 5-10 days **Sources**: Undercooked beef (especially hamburger), unpasteurized milk and juice, raw fruits and vegetables (e.g. sprouts), and contaminated water",
  "Hepatitis A" : "**Illness**: Hepatitis **Incubation**: 28 days average (15-50 days) **Symptoms**: Diarrhea, dark urine, jaundice, and flu-like symptoms, i.e., fever, headache, nausea, and abdominal pain **Duration**: Variable, 2 weeks-3 months **Sources**: Raw produce, contaminated drinking water, uncooked foods and cooked foods that are not reheated after contact with an infected food handler; shellfish from contaminated waters", 
  "Listeria Monocytogenes" : "**Illness**: Listeriosis **Incubation**: 9-48 hrs for gastrointestinal symptoms, 2-6 weeks for invasive disease **Symptoms**: Fever, muscle aches, and nausea or diarrhea. Pregnant women may have mild flu-like illness, and infection can lead to premature delivery or stillbirth. The elderly or immunocompromised patients may develop bacteremia or meningitis **Duration**: Variable **Sources**: Unpasteurized milk, soft cheeses made with unpasteurized milk, ready-to-eat deli meats",
  "Noroviruses" : "**Illness**: Variously called viral gastroenteritis, winter diarrhea, acute nonbacterial gastroenteritis, food poisoning, and food infection **Incubation**: 12-48 hrs **Symptoms**: Nausea, vomiting, abdominal cramping, diarrhea, fever, headache. Diarrhea is more prevalent in adults, vomiting more common in children **Duration**: 12-60 hrs **Sources**: Raw produce, contaminated drinking water, uncooked foods and cooked foods that are not reheated after contact with an infected food handler; shellfish from contaminated waters",
  "Salmonella" : "**Illness**: Salmonellosis **Incubation**: 6-48 hours **Symptoms**: Diarrhea, fever, abdominal cramps, vomiting **Duration**: 4-7 days **Sources**: Eggs, poultry, meat, unpasteurized milk or juice, cheese, contaminated raw fruits and vegetables",
  "Shigella" : "**Illness**: Shigellosis or Bacillary dysentery **Incubation**: 24-48 hrs **Symptoms**: Abdominal cramps, fever, and diarrhea. Stools may contain blood and mucus **Duration**: 4-7 days **Sources**: Raw produce, contaminated drinking water, uncooked foods and cooked foods that are not reheated after contact with an infected food handler",
  "Staphylococcus Aureus" : "**Illness**: Staphylococcal food poisoning **Incubation**: 1-6 hours **Symptoms**: Sudden onset of severe nausea and vomiting. Abdominal cramps. Diarrhea and fever may be present **Duration**: 24-48 hours **Sources**: Unrefrigerated or improperly refrigerated meats, potato and egg salads, cream pastries",
  "Vibrio Parahaemolyticus" : "**Illness**: V. parahaemolyticus infection **Incubation**: 4-96 hours **Symptoms**: Watery (occasionally bloody) diarrhea, abdominal cramps, nausea, vomiting, fever **Duration**: 2-5 days **Sources**: Undercooked or raw seafood, such as shellfish",
  "Vibrio Vulnificus" : "**Illness**: V. vulnificus infection **Incubation**: 1-7 days **Symptoms**: Vomiting, diarrhea, abdominal pain, bloodborne infection. Fever, bleeding within the skin, ulcers requiring surgical removal. Can be fatal to persons with liver disease or weakened immune systems **Duration**: 2-8 days **Sources**: Undercooked or raw seafood, such as shellfish (especially oysters)"
}
epidemiology_definitions = {
    "Hippocrates": "Circa 400 B.C. _ attempts to explain disease occurrence from a rational viewpoint.",
    "John Graunt": "1662 _ publishes a landmark analysis of mortality data.",
    "James Lind": "1740's _ conducts the first experiment on scurvy and discovers the preventive properties of limes.",
    "Edward Jenner": "1790's _ develops the smallpox vaccine using clinical trials with cowpox.",
    "William Farr": "1800 _ builds upon Graunt's work and develops modern vital statistics and surveillance practices.",
    "John Snow": "1849-54 _ conducts a groundbreaking study on the waterborne transmission of cholera in London.",
    "Louis Pasteur": "1880s _ identifies the bacterial cause of anthrax and develops a vaccine.",
    "Robert Koch": "1843-1910 _ formalizes standards (postulates) to identify organisms causing infectious diseases.",
    "Flu": "1910's Pandemic (Hint - Influenza)",
    "Joseph Goldberger": "1920 _ publishes a field study showing the dietary origin of pellagra.",
    "Flouride": "1940s _ supplements added to public water supplies in randomized community trials.",
    "Framingham Study": "1949 - Initiation of the __ of risk factors for cardiovascular disease.",
    "Lung Cancer": "1950 - Epidemiological studies link cigarette smoking and __ (Hint: Cancer).",
    "Salk Polio": "1954 - Field trial of the __ vaccine - the largest formal human experiment.",
    "Mantel and Haenzel": "1959 - _ develop a statistical procedure for stratified analysis of case-control studies.",
    "MacMahon": " - _ publishes the first epidemiologic text with a systematic focus on study design.",
    "Smoking": "1964 - US Surgeon General's Report on _ and Health establishes criteria for evaluation of causality.",
    "Smallpox": "1970s - Large community-based trials implemented; worldwide eradication of _.",
    "HIV": "1980's - Chronic disease, injury, and occupational epidemiology; _ epidemic.",
    "Edward Sydenstricker": "1990s _ becomes a pioneer public health statistician; focus on behavioral risk factor epidemiology.",
    "West Nile Virus": "Genetic and molecular epidemiology; health disparities; HIPAA in the USA; __ in the 2000s.",
    "9/11": "2001...Event...",
    "Anthrax and Smallpox": "Bioterrorism; _ and _ threat and vaccinations in 2002.",
    "SARS": "2003 outbreak; quarantines and public health law; worldwide epidemiology; BSE in Canada.",
    "SARS": "2004 _ recurrence; BSE in USA; flu epidemic.",
    "H1N1": "2009 _ pandemic.",
    "Epidemiology": "The study of distribution and determinants of health-related states in specified populations.",
    "Classical Epidemiology": "Population-oriented; studies community origins of health problems.",
    "Clinical Epidemiology": "Studies patients in healthcare settings to improve diagnosis and treatment.",
    "Infectious Disease Epidemiology": "Focuses on diseases caused by infectious agents.",
    "Chronic Disease Epidemiology": "Focuses on diseases with long **Duration**s and complex causes.",
    "Descriptive Epidemiology": "Involves identifying the time, place, and person involved in the onset of health-related events.",
    "Analytic Epidemiology": "Concerned with finding the causes of health-related events and identifying interventions.",
    "Biologic Agents": "Viruses or infectious agents in the body.",
    "Chemical Agents": "Substances outside the body that can cause harm.",
    "Physical Agents": "Affect outer parts of the body.",
    "Infectivity": "Pathogen causes infection.",
    "Pathogenicity": "Infection causing disease.",
    "Virulence": "Disease making an individual severely ill or leading to death.",
    "Contamination": "Pathogen comes in contact with tissues.",
    "Infection": "Damage to tissues causing infection.",
    "Disease": "Effects of damage to tissues.",
    "Cluster": "An aggregation of cases closely grouped in time and space.",
    "Endemic Disease": "Present at a continuous level throughout a population/geographic area.",
    "Epidemic": "Large numbers of people over a wide geographical area are affected.",
    "Etiology": "Study of the cause of a disease.",
    "Fomite": "A physical object that serves to transmit an infectious agent from person to person.",
    "Iatrogenic": "An **Illness** caused by medication or a physician.",
    "Incubation Period": "Time between contact with a pathogen and showing **Symptoms** of disease.",
    "Index Case": "First patient in an epidemiological study.",
    "Morbidity": "Rate of disease in a population.",
    "Mortality": "Rate of death in a population.",
    "Outbreak": "More cases of a disease than expected in a given area or among a specialized group of people.",
    "Pandemic": "An epidemic occurring over several countries or continents.",
    "Plague": "A serious, potentially life-threatening infectious disease.",
    "Nosocomial Disease": "An infection acquired in a hospital.",
    "Risk": "Probability that an individual will be affected by or die from an **Illness** or injury.",
    "Surveillance": "Systematic and ongoing collection, analysis, interpretation, and dissemination of health data.",
    "Vector": "An animal that transmits disease but is not the cause of the disease itself.",
    "Zoonosis": "An infectious disease transmissible from animals to humans.",
    "Symptomatic": "Showing **Symptoms** or signs of injury.",
    "Carrier": "Showing no signs or **Symptoms** but can be a carrier of disease.",
    "Sporadic": "A disease that occurs infrequently and irregularly.",
    "Hyperendemic": "Constant presence at high incidence and prevalence within a given geographic area or population.",
    "Hypoendemic": "A disease constantly present at a low incidence or prevalence affecting a small proportion of individuals.",
    "Holoendemic": "Characterized by the infection of essentially every individual in a defined population.",
    "Ratio": "Value obtained by dividing one quantity by another.",
    "Proportion": "Comparison of a part to the whole, expressed as a decimal, fraction, or percentage.",
    "Incidence": "Rate of occurrence of an event; number of new cases of disease over a specified period of time.",
    "Indirect Transmission": "No human-to-human contact (mainly vehicle or airborne).",
    "Direct Transmission": "Human-to-human contact.",
    "Fulminant": "Sudden severity of **Symptoms**.",
    "Idiopathic": "Of uncertain or unknown origin.",
    "Random Selection": "Choosing participants for a study randomly.",
    "Randomization": "Select which group someone in a study will be in randomly.",
    "Incubation Period": "Time in between when a person comes into contact with a pathogen and when they first show **Symptoms** or signs of disease. (latent between exposure and infection).",
    "Frequency": "Refers not only to the number of health events (i.e., disease) in a population but also to the relationship of that number to the size of the population. The resulting rate allows epidemiologists to compare disease occurrence across different populations.",
    "Pattern": "Refers to the occurrence of health-related events by epi triad. Time patterns may be any other breakdown of time that may influence disease or injury occurrence (i.e., week). Place patterns include live/work places. Personal characteristics include demographic factors/behaviors and environmental exposures.",
    "Active Immunity": "Occurs when the person is exposed to a live pathogen, develops the disease, and becomes immune as a result of the primary immune response.",
    "Passive Immunity": "Short-term immunization by the injection of antibodies, such as gamma globulin, that are not produced by the recipient's cells. Naturally acquired passive immunity occurs during pregnancy, in which certain antibodies are passed from the maternal into the fetal bloodstream.",
    "Herd Immunity": "Protecting a whole community from disease by immunizing a critical mass of its populace. Vaccination protects more than just the vaccinated person. By breaking the chain of an infection transmission, vaccination can also protect people who haven’t been immunized. But to work, this protection requires that a certain percentage of people in a population be vaccinated.",
    "Spillover": "When an animal disease spreads to humans for the first time and becomes a zoonosis.",
    "Classical Epidemiology": "Population-oriented; studies community origins of health problems related to nutrition, environment, human behavior, and the psychological, social, and spiritual state of a population. The event is more aimed towards this type of epidemiology.",
    "Clinical Epidemiology": "Studies patients in healthcare settings to improve the diagnosis and treatment of various diseases and the prognosis for patients already affected by a disease. These can be further divided into: Infectious Disease Epidemiology - dependent on laboratory support or Chronic Disease Epidemiology - dependent on complex sampling and statistical methods.",
    "Natural History of Disease": "Natural history - pathological onset -> presymptomatic -> clinically obvious -> recover/death/remission. Prognosis - prediction of course to determine treatment, considering quality/quantity of life.",
    "Efficacy": "__ - treatment will do more harm than good, needs compliance. Effectiveness means even without compliancy.",
    "Prevention": "Reduce risks before issues arise, reduce risks in patients with established disease, behavioral/pharmacological intervention.",
  "Demographic Data": "Information about the characteristics of a population, such as age, gender, income, and education.",
  "Identification Data": "Details that distinguish one individual or thing from another, often used for tracking or recognition.",
  "Risk Factors Data": "Information about conditions or behaviors that increase the likelihood of developing a disease or experiencing a health-related event.",
  "Clinical Disease Data": "Data related to the manifestation, progression, and treatment of diseases in individuals.",
  "Public Health": "The organized efforts of society to promote and protect health and prevent **Illness**, often through government-led initiatives and community actions.",
  "Clinical Care": "Prevention, treatment, and management of **Illness** and the preservation of mental and physical well-being through medical and allied health professions.",
  "Determinant": "A factor that contributes to the generation of a trait or influences health outcomes.",
  "Epidemic": "The occurrence of cases of an **Illness**, health-related behavior, or other health-related event in a community or region that exceeds normal expectancy.",
  "Health Outcome": "The result of a medical condition that directly affects the length or quality of a person’s life.",
  "Genes and Biology": "Biological factors influencing health.",
  "Health Behaviors": "Individual behaviors that impact health.",
  "Social and Societal Characteristics": "Social and community factors affecting health.",
  "Health Services": "The availability, affordability, and utilization of healthcare services.",
  "Collect Data": "Surveillance, determine Time/Place/Person triad.",
  "Assessment": "Inference.",
  "Hypothesis Testing": "Determine how and why.",
  "Action": "Intervention.",
  "Experimental Study": "A study in which investigators can control certain factors from the beginning.",
  "Observational Study": "A study where the epidemiologist does not control the circumstances; can be descriptive or analytic.",
  "Normal Flora": "Many microbes have a positive symbiotic relationship with other organisms.",
  "Mutualism": "Both organisms benefit.",
  "Commensalism": "One organism is not harmed or helped.",
  "Parasitism": "The condition where one organism is helped, and the other is harmed, which occurs when humans are invaded by infectious microbes.",
  "Timeline of Diseases": "The process from exposure to factors sufficient for disease development to the manifestation of **Symptoms**.",
  "Agent": "Microorganism causing disease.",
  "Reservoir": "Place where the microorganism can reproduce.",
  "Portal of Exit": "The set path for the agent to leave the reservoir.",
  "Mode of Transmission": "Method by which the organism is transferred.",
  "Portal of Entry": "Opening through which the agent enters the host.",
  "Susceptible Host": "A person vulnerable to infection, such as the young, elderly, or immunocompromised.",
  "Infectious Dose": "The amount of pathogen required to cause an infection in the host.",
  "Period of Communicability": "The period when an individual is infectious and can spread germs to others.",
  "Contamination": "Presence of a potentially infectious agent in the host without invading tissues.",
  "Infection": "When the infectious agent begins invasion and rapid multiplication in the host tissue.",
  "Disease": "When the cumulative effects of infection cause damage in the tissues.",
  "Infectivity": "Proportion of exposed persons who become infected.",
  "Pathogenicity": "Proportion of infected persons who develop clinical disease.",
  "Virulence": "Proportion of persons with clinical disease who become severely ill or die.",
  "Surveillance - Definition": "Provide information for health action by public health personnel, government leaders, and the public to guide public health policy and programs.",
  "Surveillance": "Identify, define, and measure the health problem of interest. Collect and compile data about the problem (and if possible, factors that influence it). Analyze and interpret these data. Provide these data and their interpretation to those responsible for controlling the health problem. Monitor and periodically evaluate the usefulness and quality of surveillance to improve it for future use (surveillance of a problem often does not include actions to control the problem).",
  "Passive Surveillance": "Diseases are reported to health care providers; simple and inexpensive.",
  "Active Surveillance": "Health agencies actively seek reports from health providers; used in epidemics or targeted elimination.",
  "Sentinel Surveillance": "Reporting by selected health professionals representing a specific area or group; can be active or passive.",
  "Syndromic Surveillance": "Focuses on **Symptoms** rather than physician-diagnosed or lab-confirmed disease; used for outbreak detection."
}
biases = {
  "Random": "Fluctuations around a value. Precision measures. ",
  "Systematic" : "Any error other than random.",
  "Selection" : "Proper randomization not achieved.",
  "Sampling": "Some members of pop less likely to be included, subtype of selection bias. undermines external validity of a test while selection bias addresses internal validity for differences insample at hand.",
  "Self-Selection" : "People who select themselves may be different",
  "Internal Validity": "Examines whetherstudy design, conduct, and analysis answer research questions without bias.", 
  "External Validity" : "Examines whetherstudy findings can be generalized to other contexts.",
  "Accumulation Effect": "Can take long time for effect to build up",
  "Allocation" : "Difference in how ppl assigned to cont or case/treatment", 
  "Ascertainment" : "Differences inidentification of individuals. some members of intended population have diff sampling probability than others", 
  "Attrition" : "Unequal loss of participants", 
  "Berksonian" : "Case control; false correlation because of diff probs of hosp admission. combination of exposure to risk and occurrence of dss increases likelihood of being admitted to hospital eg. From hospital sample, conclude that people with respiratory disease are much more likely to suffer from locomotor disease. However, community sample proves this is incorrect bc people w/ both diseases more likely to be hospitalized",
  "Channeling" : "When smthg abtpatient dictates which group they are assigned to", 
  "Chronological" : "Relationship between time of recruitment and observed outcome", 
  "Compliance" : "Compliant participants differ",
  "Confirmation" : "When a researcher uses information to confirm hypothesis",
  "Confounding" : "More than one factor affects causation of disease (Use Randomize, Restrict, or match to eliminate)",
  "Restrict" : "Prevent ppl with certain traits/behavior", 
  "Effect Modification" : "When exposure has diff effect on diff subgroups, ie multiplicative effect", 
  "Differential Misclassification" : "One way error. Cases more likely to be misqualified, etc",
  "Hawthorne Effect" : "People behave differently when watched", 
  "Healthy Worker Effect" : "Workers generally healthier", 
  "Iceberg Phenomenon" : "Only small amount of cases visible, ie HIV but no AIDS", 
  "Immortal Time" : "Misclassification of time interval", 
  "Information" : "Data intrinsically twisted by study participants",  
  "Interviewer": "Int’s prev knowledge may influence question presentation ",
  "Late look" : "Data gathered/analyzed at inappropriate time", 
  "Length Time" : "Detection of slower cases only/missing deaths", 
  "Measurement/Instrument" : "Inaccurate instruments", 
  "Neyman’s" : "Prevalence-incidence bias occurs due totiming of when cases are included in a research study. Eg study investigating pneumonia only enrols cases admitted to a hospital. Those who died prior will not be included, moderately severe, but not fatal cases.", 
  "Non-Differential Misclassification" : "Mistakes in classifying dss or exposure", 
  "Non-Response" : "Those that do not respond may be different (ie attrition)", 
  "Observer" : "Similar to confirm, aka Pygmalion/Galatea", 
  "Pygmalion/Galatea" : "High expectations → improved results. In experiments aka Rosenthal Effect. Reverse is Golem effect",  
  "Panel Effect" : "Fatigue from too many interviews",
  "Performance" : "Differences in care between study groups", 
  "Prevarication" : "(Lying) subject over- or under-estimates outcome because of knowledge of treatment",
  "Procedure" : "Lack of randomization of treatment Publication only pub favorable results",
  "Recall" : "Affected subjects may more easily recall", 
  "Reporting" : "Selective revealing or suppression of information by subjects. ***Branches:*** **Publication** (nonpublication) - studies w/ + findings more likely to be published than -/no findings . **Time Lag**  + findings likely to be pub. Faster **Duplicate Publication** studies w/ >1 pub location → higher weighting **Location** certain reports harder to find (journals easier) **Citation** + findings more likely to be cited **Language** ignoring studies not in native lang  **Outcome Reporting** selective reporting of certain outcomes",
  "Sampling" : "Occurs when some members of a population are systematically more likely to be selected in a sample than others.",
  "Simpson’s Paradox" : "Trend appears in several groups of data but disappears or reverses when combined. Eg. men appeared to be more susceptible to illness than women, but when studies were carried out, women were found to have a higher probability of contractingillness. ",
  "Social Desirability/Acceptability" : "Respond in acceptable way",
  "Surveillance/Detection" : "Known exposure/outcome followed more carefully", 
  "Transfer": "Participants lost to follow up", 
  "Workup/Lead Time" : "Actual duration of dss not changed, longer awareness from early diag", 
  "Ecological Fallacy" : "Type of logical error when relationships at group level are incorrectly assumed to hold at individual level", 
  "Aggregation Fallacy" : "Type of logical error when relationships which exist at individual level rare incorrectly assumed to hold at group level",
  "Berkson’s" : "Sampling collected from subpopulation, no pop", 
  "Convenience" : "Sample estimates are not reflective of true effects among the target population because the sample poorly represents the target population"
  
}
microbe_id = {
  "AIDS": "Virus",
  "Chicken Pox": "Virus",
  "Shingles": "Virus",
  "Common Cold": "Virus",
  "Dengue Fever": "Virus",
  "Ebola Hemorrhagic Fever": "Virus",
  "Hepatitis": "Virus",
  "Influenza": "Virus",
  "Measles": "Virus",
  "Mononucleosis": "Virus",
  "Mumps": "Virus",
  "Norovirus": "Virus",
  "Polio": "Virus",
  "Rabies": "Virus",
  "Rubella": "Virus",
  "Yellow Fever": "Virus",
  "Zika": "Virus",
  "Herpes": "Virus",
  "Smallpox": "Virus",
  "Encephalitis": "Virus",
  "Pneumonia (Viral)": "Virus",
  "West Nile Fever": "Virus",
  "Bronchitis": "Virus",
  "Lassa": "Virus",
  "SARS": "Virus",
  "Marburg Disease": "Virus",
  "Chikungunya": "Virus",
  "Haemophilus Influenzae": "Virus",
  "HPV": "Virus",
  "Monkeypox": "Virus",
  "RSV": "Virus",
  "Meningitis": "Bacteria",
  "Pneumonia (Bacterial)": "Bacteria",
  "Crown Gall Disease": "Bacteria",
  "Gonorrhea": "Bacteria",
  "Toxic Shock Syndrome": "Bacteria",
  "Typhus": "Bacteria",
  "Anthrax": "Bacteria",
  "Botulism": "Bacteria",
  "Cholera": "Bacteria",
  "Chlamydiasis": "Bacteria",
  "Dental Caries": "Bacteria",
  "Legionnaires' Disease": "Bacteria",
  "Lyme Disease": "Bacteria",
  "MRSA": "Bacteria",
  "Peptic Ulcer Disease": "Bacteria",
  "Pertussis": "Bacteria",
  "Pseudomonas Aeruginosa": "Bacteria",
  "Rocky Mountain Spotted Fever": "Bacteria",
  "Erlichiosis": "Bacteria",
  "Strep Throat": "Bacteria",
  "Syphilis": "Bacteria",
  "Tetanus": "Bacteria",
  "Anasplasmosis": "Bacteria",
  "Tuberculosis": "Bacteria",
  "Diphtheria": "Bacteria",
  "Leptospirosis": "Bacteria",
  "Meliodosis": "Bacteria",
  "Psittacosis": "Bacteria",
  "Wolbachia": "Bacteria",
  "Leprosy": "Bacteria",
  "Brucellosis": "Bacteria",
  "Athlete's Foot": "Fungi",
  "Dutch Elm Disease": "Fungi",
  "Early Potato Blight": "Fungi",
  "Histoplasmosis": "Fungi",
  "Ringworm": "Fungi",
  "Thrush": "Fungi",
  "White Nose Syndrome": "Fungi",
  "Batrachochytrium": "Fungi",
  "Ergotism": "Fungi",
  "Aspergillosis": "Fungi",
  "Cryptococcosis": "Fungi",
  "Mucormycosis": "Fungi",
  "Cryptosporidiosis": "Protozoa",
  "Cyclosporiasis": "Protozoa",
  "Babesiosis": "Protozoa",
  "Giardiasis": "Protozoa",
  "Malaria": "Protozoa",
  "Naegleria": "Protozoa",
  "Leishmaniasis": "Protozoa",
  "African Trypanosomiasis": "Protozoa",
  "Toxoplasmosis": "Protozoa",
  "Paralytic Shellfish Poisoning": "Protozoa",
  "Estuary Associated Syndrome": "Protozoa",
  "Chronic Wasting Disease": "Prion",
  "Kuru": "Prion",
  "Scrapie": "Prion",
  "Mad Cow Disease": "Prion",
  "Creutzfeldt-Jakob Disease": "Prion",
  "Gerstmann-Straussler-Scheinker syndrome": "Prion",
  "Alpers syndrome": "Prion",
  "Hookworm": "Parasitic Worm",
  "Pinworm": "Parasitic Worm",
  "Schistosomiasis": "Parasitic Worm",
  "Tapeworm": "Parasitic Worm",
  "Trichinosis": "Parasitic Worm",
  
}
correct_answers = {}
correct_answers_pathogen = {}
correct_biases = {}
correct_microbe = {}
race = 0
microbescoreShivPat = 0


@interactions.slash_command(
  name="microbescore",
  description="Shows session's microbe score",
)
async def get_score(ctx):
  global microbescoreShivPat
  await ctx.send(f"Your session microbe score is **{microbescoreShivPat}**")

@interactions.slash_command(
  name="microbesquiz",
  description="Get a random microbe from the glossary."
)
async def get_microbe(ctx):
  random_word_microbe, random_definition_microbe = random.choice(list(microbe_id.items()))
  correct_microbe[ctx.author.id] = random_definition_microbe  # Store the correct answer for the user
  await ctx.send(f"Identify: {random_word_microbe}")
@interactions.slash_command(
  name="skipmicrobe",
  description="Skip a question"
)
async def skipmicrobe(ctx):
  Answer_Microbe = correct_microbe[ctx.author.id]
  await ctx.send(f"The answer was **{Answer_Microbe.upper()}**")
  del correct_microbe[ctx.author.id]

@interactions.slash_command(
  name="hintmicrobe",
  description= "Get a hint for the definition."
)
@slash_option(
  name="type_of_hint",
  description="What type of hint would you like?",
  required=True,
  opt_type=OptionType.STRING
)
async def hintmicrobe(ctx: SlashContext, type_of_hint: str):
  if type_of_hint == "first":
    first_letter_microbe = correct_microbe[ctx.author.id][0]
    await ctx.send(f"The first letter of the word is **{first_letter_microbe}**.")
  elif type_of_hint == "last":
    last_letter_microbe = correct_microbe[ctx.author.id][-1]
    await ctx.send(f"The last letter of the word is **{last_letter_microbe}** ")
  elif type_of_hint == "count":
    count_microbe = len(correct_microbe[ctx.author.id])
    await ctx.send(f"The word has {count_microbe} letters.")
@interactions.slash_command(
  name="answermicrobe",
  description="Type your answer here."
)
@slash_option(
  name="user_answer",
  description="Your answer.",
  required=True,
  opt_type=OptionType.STRING,
)
async def microbe(ctx: SlashContext, user_answer: str):
  global microbescoreShivPat
  if ctx.author.id in correct_microbe:
    correct_answer_microbe = correct_microbe[ctx.author.id]  
    if user_answer == correct_answer_microbe:
      await ctx.send(f"Correct! The answer was **{correct_answer_microbe.upper()}**.")
      microbescoreShivPat += 1
    else:
      await ctx.send(f"Incorrect. The answer was **{correct_answer_microbe.upper()}**. ")
    del correct_microbe[ctx.author.id]  
  else:
    await ctx.send("No question has been asked. Use /microbequiz to get a question.")

@interactions.slash_command(
  name="vocabquiz",
  description="Get a random definition from the glossary."
)
async def get_definition(ctx):
  random_word, random_definition = random.choice(list(epidemiology_definitions.items()))
  correct_answers[ctx.author.id] = random_word  # Store the correct answer for the user
  await ctx.send(f"Definition: {random_definition}")
@interactions.slash_command(
  name="skipvocab",
  description="Skip a question"
)
async def skipvocab(ctx):
  Answer = correct_answers[ctx.author.id]
  await ctx.send(f"The answer was **{Answer.upper()}**")
  del correct_answers[ctx.author.id]

@interactions.slash_command(
  name="hintvocab",
  description= "Get a hint for the definition."
)
@slash_option(
  name="type_of_hint",
  description="What type of hint would you like?",
  required=True,
  opt_type=OptionType.STRING
)
async def hintvocab(ctx: SlashContext, type_of_hint: str):
  if type_of_hint == "first":
    first_letter = correct_answers[ctx.author.id][0]
    await ctx.send(f"The first letter of the word is **{first_letter}**.")
  elif type_of_hint == "last":
    last_letter = correct_answers[ctx.author.id][-1]
    await ctx.send(f"The last letter of the word is **{last_letter}** ")
  elif type_of_hint == "count":
    count = len(correct_answers[ctx.author.id])
    await ctx.send(f"The word has {count} letters.")
@interactions.slash_command(
  name="answervocab",
  description="Type your answer here."
)
@slash_option(
  name="user_answer",
  description="Your answer.",
  required=True,
  opt_type=OptionType.STRING,
)
async def word(ctx: SlashContext, user_answer: str):
  if ctx.author.id in correct_answers:
    correct_answer = correct_answers[ctx.author.id]  
    if user_answer == correct_answer:
      await ctx.send(f"Correct! The answer was **{correct_answer.upper()}**.")
    else:
      await ctx.send(f"Incorrect. The answer was **{correct_answer.upper()}**.")
    del correct_answers[ctx.author.id]  
  else:
    await ctx.send("No question has been asked. Use /vocabquiz to get a question.")

@interactions.slash_command(
  name="pathogenquiz",
  description="Get a random definition from the pathogen glossary."
)
async def get_pathogen(ctx):
  random_word_lab, random_definition_lab = random.choice(list(disease_lab.items()))
  correct_answers_pathogen[ctx.author.id] = random_word_lab  # Store the correct answer for the user
  await ctx.send(f"Crack the case!: {random_definition_lab}")
@interactions.slash_command(
  name="skipagent",
  description="Skip a question"
)
async def skipagent(ctx):
  Answer_lab = correct_answers_pathogen[ctx.author.id]
  await ctx.send(f"The answer was **{Answer_lab.upper()}**")
  del correct_answers_pathogen[ctx.author.id]

@interactions.slash_command(
  name="hintpathogen",
  description= "Get a hint for the pathogen."
)
@slash_option(
  name="type_of_hint_pathogen",
  description="What type of hint would you like?",
  required=True,
  opt_type=OptionType.STRING
)
async def hintpathogen(ctx: SlashContext, type_of_hint_pathogen: str):
  if type_of_hint_pathogen == "first":
    first_letter_pathogen = correct_answers_pathogen[ctx.author.id][0]
    await ctx.send(f"The first letter of the word is **{first_letter_pathogen}**.")
  elif type_of_hint_pathogen == "last":
    last_letter_pathogen = correct_answers_pathogen[ctx.author.id][-1]
    await ctx.send(f"The last letter of the word is **{last_letter_pathogen}** ")
  elif type_of_hint_pathogen == "count":
    count_pathogen = len(correct_answers_pathogen[ctx.author.id])
    await ctx.send(f"The word has {count_pathogen} letters.")
@interactions.slash_command(
  name="answerpathogen",
  description="Type your answer here."
)
@slash_option(
  name="user_answer_pathogen",
  description="Your answer.",
  required=True,
  opt_type=OptionType.STRING,
)
async def pathogen(ctx: SlashContext, user_answer_pathogen: str):
  if ctx.author.id in correct_answers_pathogen:
    correct_answer_pathogen = correct_answers_pathogen[ctx.author.id]  
    if user_answer_pathogen == correct_answer_pathogen:
      await ctx.send(f"Correct! The answer was **{correct_answer_pathogen.upper()}**.")
    else:
      await ctx.send(f"Incorrect. The answer was **{correct_answer_pathogen.upper()}**.")
    del correct_answers_pathogen[ctx.author.id]  
  else:
    await ctx.send("No question has been asked. Use /pathogenquiz to get a question.")

@interactions.slash_command(name="testing",description="test works!")
async def test_command(ctx: SlashContext):
    await ctx.send("Bot is working!")
  
@interactions.slash_command(name="oddsratio",description="Calculate Odds ratio by inputting the 4 numbers a b c d")
@slash_option(
    name="option_1",
    description="Letter A",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_2",
    description="Letter B",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_3",
    description="Letter C",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_4",
    description="Letter D",
    required=True,
    opt_type=OptionType.INTEGER,
)
async def oddsr(ctx: SlashContext, option_1: int, option_2: int, option_3: int, option_4: int):
    odds_ratio = ((int(option_1)*int(option_4))/(int(option_2)*int(option_3)))
    await ctx.send(f"Odds Ratio is {odds_ratio}. This study is a Case-Control Study. Works backward from effect or **Illness** to suspected cause. Control group is a selected group who has similar characteristics to the sick group but is not ill. They are then checked for similar exposures. It is often hard to select the control group for this type of study. Odds Ratio is calculated to evaluate the possible agents & vehicles of transmission. Odds ratio proves that people who were exposed to the reservoir has {odds_ratio} times chances to get the disease than those unexposed")

@interactions.slash_command(name="relativerisk",description="Calculate Relative Risk by inputting the 4 numbers a b c d")
@slash_option(
    name="option_1",
    description="Letter A",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_2",
    description="Letter B",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_3",
    description="Letter C",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_4",
    description="Letter D",
    required=True,
    opt_type=OptionType.INTEGER,
)
async def rr(ctx: SlashContext, option_1: int, option_2: int, option_3: int, option_4: int):
    relative_risk = (int(option_1)/(int(option_1)+int(option_2)))/(int(option_3)/(int(option_3)+int(option_4)))
    if relative_risk == 1:
        await ctx.send(f"Relative Risk Ratio is {relative_risk}. This study is a Cohort Study. A relative risk = 1.0 indicates that the incidence rates of disease in the exposed group is equal to the incidence rates in unexposed group. Therefore the data does not provide evidence for an association. Based upon exposure status whether or not they have outcome (**Illness**); used with a small well-defined population and moves forward from exposure.")
    elif relative_risk > 1:
        await ctx.send(f"Relative Risk Ratio is {relative_risk}. This study is a Cohort Study. A relative risk >1.0 indicates a positive association or an increased risk. This risk increases in strength as the magnitude of the relative risk increases. Based upon exposure status whether or not they have outcome (**Illness**); used with a small well-defined population and moves forward from exposure.")
    else:
        await ctx.send(f"Relative Risk Ratio is {relative_risk}. This study is a Cohort Study. The data indicates a negative association or decreased risk (possible protective effect) if the relative risk is between 0 and 1.0. Relative risk is not expressed in negative numbers. Based upon exposure status whether or not they have outcome (**Illness**); used with a small well-defined population and moves forward from exposure.")



@interactions.slash_command(name="ppv",description="Calculate PPV using the 2 numbers a b")
@slash_option(
    name="option_1",
    description="Letter A",
    required=True,
    opt_type=OptionType.INTEGER,
)
@slash_option(
    name="option_2",
    description="Letter B",
    required=True,
    opt_type=OptionType.INTEGER,
)
async def ppv(ctx: SlashContext, option_1:int, option_2:int):
    PPV = (int(option_1)/(int(option_1)+int(option_2)))
    await ctx.send(f"PPV is {PPV}")

@interactions.slash_command(name="npv",description="Calculate NPV using the 2 numbers c d")
@slash_option(
  name="option_3",
  description="Letter C",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_4",
  description="Letter D",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def npv(ctx: SlashContext, option_3:int, option_4:int):
  NPV = (int(option_3)/(int(option_3)+int(option_4)))
  await ctx.send(f"NPV is {NPV}")

@interactions.slash_command(name="sensitivity",description="Calculate sensitivity using a and c")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_3",
  description="Letter C",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def sens(ctx: SlashContext, option_1:int, option_3:int):
    Sensitivity = (int(option_1)/(int(option_1)+int(option_3)))
    if Sensitivity < 0.5:
        await ctx.send(f"Sensitivity is {Sensitivity}. This test does a mid job of determining disease")
    else:
        await ctx.send(f"Sensitivity is {Sensitivity}. This test does a good job of determining disease.")

@interactions.slash_command(name="specificity",description="Calculate specificity using b and d as the 2 numbers")
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_4",
  description="Letter D",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def spec(ctx: SlashContext, option_2:int, option_4:int):
    Specificity = (int(option_4)/(int(option_4)+int(option_2)))
    if Specificity < 0.5:
        await ctx.send(f"Specificity is {Specificity}. This can't determine negative results.")
    else:
        await ctx.send(f"Specificity is {Specificity}. Glad you can determine negative results.")
@interactions.slash_command(name="attack_rate_exposed",description="Calculate Attack rate for the exposed by inputting a and b")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def are(ctx: SlashContext, option_1:int, option_2:int):
    AttackRateExposed = (int(option_1)/(int(option_1)+int(option_2))) * 100
    if AttackRateExposed > 50:
        await ctx.send(f"Attack Rate for Exposed is {AttackRateExposed}. This should be higher than unexposed. This is also known as Risk Ratio for Exposed.")
    else:
        await ctx.send(f"Attack Rate for Exposed is {AttackRateExposed} This is also known as Risk Ratio for Exposed. Oh gosh... Too Low")

@interactions.slash_command(name="attack_rate_unexposed",description="Calculate Attack Rate for unexposed by inputting c and d")
@slash_option(
  name="option_3",
  description="Letter C",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_4",
  description="Letter D",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def aru(ctx: SlashContext, option_3:int, option_4:int):
  AttackRateUnexposed = (int(option_3)/(int(option_3)+int(option_4))) * 100
  if AttackRateUnexposed < 50:
    await ctx.send(f"Attack Rate for Unexposed is {AttackRateUnexposed}. This is what we need.This is also known as Risk Ratio for Unexposed.")
  else:
    await ctx.send(f"Attack Rate for Unexposed is {AttackRateUnexposed}. Having a high Attack rate of unexposed is not good. This is also known as Risk Ratio for Unexposed.")
@interactions.slash_command(name="incidence",description="Calculate Incidence by inputting a and b")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def inci(ctx: SlashContext, option_1:int, option_2:int):
    Incidence = (int(option_1)/(int(option_1)+int(option_2)))
    await ctx.send(f"Incidence is {Incidence}. Now remember, Incidence happens at a specific time period, so people who got that disease from before that time period don't count here. If you happened to make that mistake, please rerun this command with correct inputs.")

@interactions.slash_command(name="point_prevalence",description="Calculate Point Prevalence by inputting a and b")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def pointp(ctx: SlashContext, option_1:int, option_2:int):
    PointPrevalence = (int(option_1)/(int(option_1)+int(option_2)))
    await ctx.send(f"Point Prevalence is {PointPrevalence}. Remember that Point prevalence shows how many people have to disease at a given point of time.. This is more prospective than retrospective")

@interactions.slash_command(name="period_prevalence",description="Calculate Period Prevalence by inputting a and b")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def periodp(ctx: SlashContext, option_1:int, option_2:int):
    PeriodPrevalence = (int(option_1)/(int(option_1)+int(option_2)))
    await ctx.send(f"Period Prevalence is {PeriodPrevalence}. Remember that Period Prevalence shows how many people have or had the disease regardless of time. This is more retrospective.")

@interactions.slash_command(name="prevalence",description="Calculate prevalence for 2x2 tables by inputting 4 numbers")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_3",
  description="Letter C",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_4",
  description="Letter D",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def prevalence(ctx: SlashContext, option_1: int, option_2: int, option_3: int, option_4: int):
  Prevalence = (int(option_1)+int(option_3))/(int(option_1)+int(option_2)+int(option_3)+int(option_4))
  await ctx.send(f"Prevalence is {Prevalence}.")
@interactions.slash_command(name="excess_risk", description="Calculate excess risk by inputting the 4 numbers a b c and d")
@slash_option(
  name="option_1",
  description="Letter A",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Letter B",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_3",
  description="Letter C",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_4",
  description="Letter D",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def er(ctx: SlashContext, option_1: int, option_2: int, option_3: int, option_4: int):
    ERisk = (int(option_1)/(int(option_1)+int(option_2)))-(int(option_3)/(int(option_3)+int(option_4)))
    await ctx.send(f"ExcessRisk is {ERisk}")
@interactions.slash_command(name="shutup",description="Delete Msgs")
@slash_option(
    name="purge_number",
    description="Amount of Msgs you would like to purge",
    required=True,
    opt_type=OptionType.INTEGER,
)
async def shutup(ctx: SlashContext, purge_number: int):
    await ctx.channel.purge(int(purge_number))
    await asyncio.sleep(3)
    await ctx.send(f"{ctx.author.mention} Deleted {purge_number} Msgs")
@interactions.slash_command(name="divide",description="Divide")
@slash_option(
  name="option_1",
  description="Number",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Divide By",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def division(ctx: SlashContext, option_1:int, option_2:int):
    Divide = (int(option_1)/int(option_2))
    await ctx.send(f"The Answer is {Divide}")
@interactions.slash_command(name="multiply",description="Multiply")
@slash_option(
  name="option_1",
  description="Number",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Multiply By",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def multiplication(ctx: SlashContext, option_1:int, option_2:int):
    Multiply = (int(option_1) * int(option_2))
    await ctx.send(f"The Answer is {Multiply}")
@interactions.slash_command(name="add",description="Addition")
@slash_option(
  name="option_1",
  description="Number",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Add to",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def addition(ctx: SlashContext, option_1:int, option_2:int):
    Sum = (int(option_1) + int(option_2))
    await ctx.send(f"The Answer is {Sum}")
@interactions.slash_command(name="subtract",description="Subtract")
@slash_option(
  name="option_1",
  description="Number",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Subtract By",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def subtraction(ctx: SlashContext, option_1:int, option_2:int):
    Subtracted = (int(option_1) - int(option_2))
    await ctx.send(f"The Answer is {Subtracted}")
@interactions.slash_command(name="exponential",description="exponential")
@slash_option(
  name="option_1",
  description="Base",
  required=True,
  opt_type=OptionType.INTEGER,
)
@slash_option(
  name="option_2",
  description="Exponent",
  required=True,
  opt_type=OptionType.INTEGER,
)
async def exponent(ctx: SlashContext, option_1:int, option_2:int):
    Exponent = (int(option_1)^int(option_2))
    await ctx.send(f"The Answer is {Exponent}")

# Devil Commands
@robot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason=None):
  if reason == None:
    reason = "no reason provided"
  await ctx.guild.kick(member)
  await ctx.send(f"User {member.mention} has been kicked for {reason}")

@robot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, ban_member:discord.Member, *, reasoning=None):
  if reasoning == None:
    reasoning = "no reason provided"
  await ctx.guild.ban(ban_member)
  await ctx.send(f"User {ban_member.mention} has been banned for {reasoning}")


@interactions.slash_command(
  name="biasquiz",
  description="Get a random bias from the glossary."
)
async def get_bias(ctx):
  random_word_bias, random_definition_bias = random.choice(list(biases.items()))
  correct_biases[ctx.author.id] = random_word_bias  # Store the correct answer for the user
  await ctx.send(f"Definition: {random_definition_bias}")
@interactions.slash_command(
  name="skipbias",
  description="Skip a question"
)
async def skipbias(ctx):
  Answer_Bias = correct_biases[ctx.author.id]
  await ctx.send(f"The answer was **{Answer_Bias.upper()}**")
  del correct_biases[ctx.author.id]

@interactions.slash_command(
  name="hintbias",
  description= "Get a hint for the definition."
)
@slash_option(
  name="type_of_hint",
  description="What type of hint would you like?",
  required=True,
  opt_type=OptionType.STRING
)
async def hintbias(ctx: SlashContext, type_of_hint: str):
  if type_of_hint == "first":
    first_letter_bias = correct_biases[ctx.author.id][0]
    await ctx.send(f"The first letter of the word is **{first_letter_bias}**.")
  elif type_of_hint == "last":
    last_letter_bias = correct_answers[ctx.author.id][-1]
    await ctx.send(f"The last letter of the word is **{last_letter_bias}** ")
  elif type_of_hint == "count":
    count_bias = len(correct_biases[ctx.author.id])
    await ctx.send(f"The word has {count_bias} letters.")
@interactions.slash_command(
  name="answerbias",
  description="Type your answer here."
)
@slash_option(
  name="user_answer",
  description="Your answer.",
  required=True,
  opt_type=OptionType.STRING,
)
async def bias(ctx: SlashContext, user_answer: str):
  if ctx.author.id in correct_biases:
    correct_answer_bias = correct_biases[ctx.author.id]  
    if user_answer == correct_answer_bias:
      await ctx.send(f"Correct! The answer was **{correct_answer_bias.upper()}**.")
    else:
      await ctx.send(f"Incorrect. The answer was **{correct_answer_bias.upper()}**.")
    del correct_biases[ctx.author.id]  
  else:
    await ctx.send("No question has been asked. Use /biasquiz to get a question.")

# robot.run("MTE2NTg4MjI2OTkwMzM3MjMxOQ.GQAguS.fuwsI9nAzGM5nZ4tZLJHeH2Dull4ddo2AStP-Y") # Uncomment this line to run devil commands. You must comment out study commands
bot.start() # Uncomment this line to run study commands. Commend out devil lines.
