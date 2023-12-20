-- Deck 1: Basic Chemistry
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basic Chemistry', 'Introduction to fundamental concepts of chemistry.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is the atomic number?', 'Number of protons in the nucleus of an atom.', 1),
('Define covalent bond.', 'A chemical bond formed by the sharing of electron pairs between atoms.', 1),
('What is Avogadro’s number?', '6.022 x 10^23 particles/mole, represents the number of particles in one mole of a substance.', 1),
('Define molarity.', 'The concentration of a solution expressed as the number of moles of solute per liter of solution.', 1),
('What is the pH scale?', 'A scale used to specify the acidity or basicity of an aqueous solution.', 1),
('Define a catalyst.', 'A substance that speeds up a chemical reaction without being consumed.', 1),
('What are isotopes?', 'Atoms of the same element with different numbers of neutrons.', 1),
('Define electrolysis.', 'The process of using electricity to drive a non-spontaneous chemical reaction.', 1),
('What is the ideal gas law?', 'PV = nRT, where P is pressure, V is volume, n is moles of gas, R is the gas constant, and T is temperature.', 1),
('What is a buffer solution?', 'A solution that can resist changes in pH upon the addition of an acid or a base.', 1);

-- Linking cards to Deck 1 (Basic Chemistry)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1);

-- Deck 2: Introduction to Programming
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Programming', 'Fundamentals of programming using Python.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is a variable in programming?', 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.', 1),
('Define a function in Python.', 'A block of code which only runs when it is called. It can pass data, known as parameters, into a function.', 1),
('What is a loop in programming?', 'A sequence of instructions that is continually repeated until a certain condition is reached.', 1),
('Explain the concept of an algorithm.', 'A step-by-step procedure for solving a problem or accomplishing some end.', 1),
('What is a conditional statement in Python?', 'Used to perform different actions based on different conditions, e.g., if, elif, else.', 1),
('Define object-oriented programming.', 'A programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields, and code, in the form of procedures.', 1),
('What is an exception in Python?', 'An error that occurs during the execution of a program. Python uses try... except blocks to handle exceptions.', 1),
('What does 'for' loop do in Python?', 'Iterates over a sequence (like a list, tuple, dictionary, set, or string) and executes code for each item.', 1),
('What is a class in Python?', 'A blueprint for creating objects (a particular data structure), providing initial values for state (member variables) and implementations of behavior (member functions, methods).', 1),
('Explain the concept of inheritance in programming.', 'A mechanism where a new class is derived from an existing class. The new class is called derived (or child) class, and the one from which it inherits is called the base (or parent) class.', 1);

-- Linking cards to Deck 2 (Introduction to Programming)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2);

-- Deck 3: World History Overview
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('World History Overview', 'A brief overview of major events in world history.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What was the Renaissance?', 'A period in European history marking the transition from the Middle Ages to modernity, characterized by an emphasis on classical culture, humanism, and a surge in artistic, cultural, and intellectual development.', 1),
('Who was Alexander the Great?', 'An ancient Macedonian ruler known for creating one of the largest empires in the ancient world by the age of 30.', 1),
('What caused World War I?', 'A complex series of events, but it is generally believed that the immediate cause was the assassination of Archduke Franz Ferdinand of Austria-Hungary.', 1),
('What was the Industrial Revolution?', 'A period of major industrialization from the late 1700s to the early 1800s which saw the introduction of machinery, predominantly in Europe and North America.', 1),
('What was the significance of the French Revolution?', 'It brought down the French monarchy, established a republic, catalyzed violent periods of political turmoil, and finally culminated in a dictatorship under Napoleon.', 1),
('Describe the Cold War.', 'A period of geopolitical tension between the Soviet Union and the United States and their respective allies, the Eastern Bloc and the Western Bloc, after World War II.', 1),
('What was the Silk Road?', 'An ancient network of trade routes connecting the East and West, important for cultural, commercial, and technological exchange.', 1),
('Who was Genghis Khan?', 'The founder and first Great Khan of the Mongol Empire, which became the largest contiguous empire in history after his death.', 1),
('What was the significance of the Magna Carta?', 'A charter of rights agreed to by King John of England in 1215, widely seen as an early step in the development of constitutional government.', 1),
('Explain the impact of the discovery of the New World.', 'It led to the exchange of goods and ideas between the Americas and the Old World and had a profound impact on the history of the world, particularly regarding colonization and trade.', 1);

-- Linking cards to Deck 3 (World History Overview)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3), (28, 3), (29, 3), (30, 3);

-- Deck 4: Basic Economics
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basic Economics', 'Fundamental concepts in economics.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Define "Economics".', 'The study of how societies use scarce resources to produce valuable commodities and distribute them among different people.', 1),
('What is "GDP"?', 'Gross Domestic Product, the total value of goods produced and services provided in a country during one year.', 1),
('Explain "Inflation".', 'The rate at which the general level of prices for goods and services is rising, and, subsequently, purchasing power is falling.', 1),
('What is "Supply and Demand"?', 'A model of price determination in a market; prices are determined by the relationship between supply and demand.', 1),
('Define "Monopoly".', 'A market structure characterized by a single seller, selling a unique product in the market.', 1),
('What is "Fiscal Policy"?', "Government adjustments to its spending levels and tax rates to monitor and influence a nation's economy.", 1),
('Explain "Macroeconomics".', 'The part of economics concerned with large-scale or general economic factors, such as interest rates and national productivity.', 1),
('What is "Microeconomics"?', 'The part of economics concerned with single factors and the effects of individual decisions.', 1),
('Define "Opportunity Cost".', 'The loss of potential gain from other alternatives when one alternative is chosen.', 1),
('What is "Elasticity" in economics?', 'A measure of how much buyers and sellers respond to changes in market conditions.', 1);

-- Linking Cards to Deck 4: Basic Economics
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(31, 4), (32, 4), (33, 4), (34, 4), (35, 4), 
(36, 4), (37, 4), (38, 4), (39, 4), (40, 4);

-- Deck 5: Advanced Mathematics
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Advanced Mathematics', 'Complex mathematical theories and applications.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Define "Integral Calculus".', 'The study of the accumulation of quantities, such as areas under a curve, and their properties.', 1),
('What is "Differential Calculus"?', 'The study of rates at which quantities change.', 1),
('Explain "Linear Algebra".', 'The branch of mathematics concerning linear equations, linear functions, and their representations in vector spaces and through matrices.', 1),
('What is a "Matrix" in mathematics?', 'A rectangular array of numbers, symbols, or expressions, arranged in rows and columns.', 1),
('Define "Vector Space".', 'A collection of objects called vectors, which may be added together and multiplied by numbers, called scalars.', 1),
('Explain "Complex Numbers".', 'Numbers that consist of a real and an imaginary part and are written in the form a + bi.', 1),
('What is "Fourier Transform"?', 'A mathematical transform that decomposes functions depending on space or time into functions depending on spatial or temporal frequency.', 1),
('Define "Topology".', 'The mathematical study of shapes and topological spaces.', 1),
('What is "Set Theory"?', 'The branch of mathematical logic that studies sets, which are collections of objects.', 1),
('Explain "Probability Theory".', 'The branch of mathematics concerned with probability, the analysis of random phenomena.', 1);

-- Linking Cards to Deck 5: Advanced Mathematics
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(41, 5), (42, 5), (43, 5), (44, 5), (45, 5), 
(46, 5), (47, 5), (48, 5), (49, 5), (50, 5);

-- Deck 6: Introduction to Philosophy
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Philosophy', 'Exploring fundamental philosophical questions and thinkers.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Philosophy"?', 'The study of general and fundamental questions, such as those about existence, reason, knowledge, values, and language.', 1),
('Who was Socrates?', 'A classical Greek philosopher credited as one of the founders of Western philosophy.', 1),
('Define "Existentialism".', 'A philosophical theory or approach that emphasizes individual existence, freedom, and choice.', 1),
('What did Plato write about?', 'Plato was a student of Socrates and wrote on a wide range of topics including political philosophy, ethics, and metaphysics.', 1),
('Who was Friedrich Nietzsche?', 'A German philosopher who wrote critically about religion, morality, culture, philosophy, and science.', 1),
('Define "Utilitarianism".', 'The doctrine that actions are right if they are useful or for the benefit of a majority.', 1),
('Explain "Epistemology".', 'The branch of philosophy concerned with the theory of knowledge.', 1),
('What is "Metaphysics"?', 'A branch of philosophy that explores the fundamental nature of reality.', 1),
('Who was Immanuel Kant?', 'A German philosopher who is a central figure in modern philosophy, known for his works in epistemology, ethics, and metaphysics.', 1),
('Define "Aesthetics".', 'The branch of philosophy dealing with the nature of beauty, art, and taste, with the creation and appreciation of beauty.', 1);

-- Linking Cards to Deck 6: Introduction to Philosophy
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(51, 6), (52, 6), (53, 6), (54, 6), (55, 6), 
(56, 6), (57, 6), (58, 6), (59, 6), (60, 6);


-- Deck 7: Introduction to Computer Science
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Computer Science', 'Foundational concepts in computer science and programming.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Computer Science"?', 'The study of both computer hardware and software design, encompassing theoretical algorithms and the practical problems of implementing them.', 1),
('Define "Algorithm".', 'A set of instructions designed to perform a specific task.', 1),
('Explain "Machine Learning".', 'A branch of artificial intelligence based on the idea that systems can learn from data, identify patterns, and make decisions with minimal human intervention.', 1),
('What is "Object-Oriented Programming"?', 'A programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields, and code, in the form of procedures.', 1),
('Define "Database".', 'An organized collection of data, generally stored and accessed electronically from a computer system.', 1),
('What is "Artificial Intelligence"?', 'The simulation of human intelligence in machines that are programmed to think and learn like humans.', 1),
('Explain "Operating System".', 'System software that manages computer hardware, software resources, and provides common services for computer programs.', 1),
('What is "Big Data"?', 'Extremely large data sets that may be analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions.', 1),
('Define "Network Security".', 'The practice of preventing and protecting against unauthorized intrusion into corporate networks.', 1),
('Explain "Blockchain Technology".', 'A decentralized, distributed ledger technology that records the provenance of a digital asset.', 1);

-- Linking Cards to Deck 7: Introduction to Computer Science
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(61, 7), (62, 7), (63, 7), (64, 7), (65, 7), 
(66, 7), (67, 7), (68, 7), (69, 7), (70, 7);

-- Deck 8: Basics of Psychology
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basics of Psychology', 'An introduction to psychological theories and practices.', 1);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Psychology"?', 'The scientific study of the mind and behavior.', 1),
('Define "Behaviorism".', 'A theory of learning based on the idea that all behaviors are acquired through conditioning.', 1),
('Explain "Cognitive Psychology".', 'The study of mental processes such as "attention, language use, memory, perception, problem-solving, creativity, and thinking."', 1),
('What is "Psychoanalysis"?', 'A set of psychological and psychotherapeutic theories and associated techniques, originally popularized by Austrian neurologist Sigmund Freud.', 1),
('Define "Humanistic Psychology".', 'A perspective that emphasizes looking at the whole individual and stresses concepts such as free will, self-efficacy, and self-actualization.', 1),
('What is "Developmental Psychology"?', 'The scientific study of how and why human beings change over the course of their life.', 1),
("Explain 'Social Psychology'.", "The scientific study of how people's thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others.", 1),
('What is "Neuropsychology"?', 'The study of the relationship between behavior, emotion, and cognition on the one hand, and brain function on the other.', 1),
('Define "Forensic Psychology".', 'The intersection between psychology and the justice system. It involves understanding fundamental legal principles, particularly with regard to expert witness testimony and the specific content area of concern.', 1),
('Explain "Positive Psychology".', 'The study of "positive subjective experience, positive individual traits, and positive institutions" and it promises to improve quality of life.', 1);

-- Linking Cards to Deck 8: Basics of Psychology
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(71, 8), (72, 8), (73, 8), (74, 8), (75, 8), 
(76, 8), (77, 8), (78, 8), (79, 8), (80, 8);

-- Deck 9
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to French Translation', 'Deck for translating common English phrases and words into French.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Bonjour', 1),
('Goodbye', 'Au revoir', 1),
('Please', 'S'il vous plaît', 1),
('Thank you', 'Merci', 1),
('Yes', 'Oui', 1),
('No', 'Non', 1),
('How are you?', 'Comment ça va?', 1),
('I am fine', 'Je vais bien', 1),
('What is your name?', 'Comment vous appelez-vous?', 1),
('My name is...', 'Je m'appelle...', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(81, 9), (82, 9), (83, 9), (84, 9), (85, 9), 
(86, 9), (87, 9), (88, 9), (89, 9), (90, 9);

-- Deck 10
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to French - Fruits', 'Translate fruit names from English to French.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Apple', 'Pomme', 1),
('Banana', 'Banane', 1),
('Grape', 'Raisin', 1),
('Orange', 'Orange', 1),
('Pineapple', 'Ananas', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(91, 10), (92, 10), (93, 10), (94, 10), (95, 10);

-- Deck 11
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('French to English - Fruits', 'Translate fruit names from French to English.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Pomme', 'Apple', 1),
('Banane', 'Banana', 1),
('Raisin', 'Grape', 1),
('Orange', 'Orange', 1),
('Ananas', 'Pineapple', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(96, 11), (97, 11), (98, 11), (99, 11), (100, 11);

-- Deck 12
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Spanish to English - Fruits', 'Translate fruit names from Spanish to English.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Manzana', 'Apple', 1),
('Plátano', 'Banana', 1),
('Uva', 'Grape', 1),
('Naranja', 'Orange', 1),
('Piña', 'Pineapple', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(101, 12), (102, 12), (103, 12), (104, 12), (105, 12);

-- Deck 13
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to English - Fruits', 'Learn synonyms or descriptions of fruits in English.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Apple', 'A round fruit with red, yellow, or green skin.', 1),
('Banana', 'A long curved yellow fruit.', 1),
('Grape', 'A small juicy fruit, typically purple or green.', 1),
('Orange', 'A citrus fruit with a tough bright orange skin.', 1),
('Pineapple', 'A tropical fruit with a rough green or brown skin.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(111, 14), (112, 14), (113, 14), (114, 14), (115, 14);

-- Deck 14
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Learning Verbs in English', 'Study and learn common English verbs.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Run', 'Move at a speed faster than a walk.', 1),
('Jump', 'Push oneself off a surface into the air by using the muscles in one’s legs.', 1),
('Read', 'Look at and comprehend the meaning of written or printed matter.', 1),
('Write', 'Mark coherent words on paper.', 1),
('Speak', 'Talk; use vocal sounds to express thoughts or feelings.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(111, 14), (112, 14), (113, 14), (114, 14), (115, 14);

-- Deck 15
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Fill in the Blank - Single Word', 'Complete the sentence by filling in a single word.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('An apple a day keeps the ___ away.', 'doctor', 1),
('Better late than ___ .', 'never', 1),
('Actions speak louder than ___ .', 'words', 1),
('The early bird catches the ___ .', 'worm', 1),
('A picture is worth a thousand ___ .', 'words', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(116, 15), (117, 15), (118, 15), (119, 15), (120, 15);

-- Deck 16
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic German Vocabulary', 'Learn basic German vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Hallo', 1),
('Goodbye', 'Auf Wiedersehen', 1),
('Thank you', 'Danke', 1),
('Yes', 'Ja', 1),
('No', 'Nein', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(121, 16), (122, 16), (123, 16), (124, 16), (125, 16);

-- Deck 17
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic Spanish Vocabulary', 'Learn basic Spanish vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Hola', 1),
('Goodbye', 'Adiós', 1),
('Thank you', 'Gracias', 1),
('Yes', 'Sí', 1),
('No', 'No', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(126, 17), (127, 17), (128, 17), (129, 17), (130, 17);

-- Deck 18
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic French Vocabulary', 'Learn basic French vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Bonjour', 1),
('Goodbye', 'Au revoir', 1),
('Thank you', 'Merci', 1),
('Yes', 'Oui', 1),
('No', 'Non', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(131, 18), (132, 18), (133, 18), (134, 18), (135, 18);

-- Deck 19
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced German Vocabulary', 'Learn advanced German vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Freiheit', 1),
('Experience', 'Erfahrung', 1),
('Knowledge', 'Wissen', 1),
('Strength', 'Stärke', 1),
('Happiness', 'Glück', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(136, 19), (137, 19), (138, 19), (139, 19), (140, 19);

-- Deck 20
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('German Phrases for Travelers', 'Essential phrases for travelers in German.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', 'Wo ist die Toilette?', 1),
('How much does this cost?', 'Wie viel kostet das?', 1),
('Can you help me?', 'Können Sie mir helfen?', 1),
('I would like a coffee.', 'Ich möchte einen Kaffee.', 1),
('I do not understand.', 'Ich verstehe nicht.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(141, 20), (142, 20), (143, 20), (144, 20), (145, 20);

-- Deck 21
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced Spanish Vocabulary', 'Learn advanced Spanish vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Libertad', 1),
('Experience', 'Experiencia', 1),
('Knowledge', 'Conocimiento', 1),
('Strength', 'Fuerza', 1),
('Happiness', 'Felicidad', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(146, 21), (147, 21), (148, 21), (149, 21), (150, 21);

-- Deck 22
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Spanish Phrases for Travelers', 'Essential phrases for travelers in Spanish.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', '¿Dónde está el baño?', 1),
('How much does this cost?', '¿Cuánto cuesta esto?', 1),
('Can you help me?', '¿Puede ayudarme?', 1),
('I would like a coffee.', 'Me gustaría un café.', 1),
('I do not understand.', 'No entiendo.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(151, 22), (152, 22), (153, 22), (154, 22), (155, 22);

-- Deck 23
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced French Vocabulary', 'Learn advanced French vocabulary words.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Liberté', 1),
('Experience', 'Expérience', 1),
('Knowledge', 'Connaissance', 1),
('Strength', 'Force', 1),
('Happiness', 'Bonheur', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(156, 23), (157, 23), (158, 23), (159, 23), (160, 23);

-- Deck 24
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('French Phrases for Travelers', 'Essential phrases for travelers in French.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', 'Où sont les toilettes?', 1),
('How much does this cost?', 'Combien cela coûte-t-il?', 1),
('Can you help me?', 'Pouvez-vous m’aider?', 1),
('I would like a coffee.', 'Je voudrais un café.', 1),
('I do not understand.', 'Je ne comprends pas.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(161, 24), (162, 24), (163, 24), (164, 24), (165, 24);

-- Deck 25
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('German Conversation Practice', 'Practice conversational phrases in German.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('How are you?', 'Wie geht es Ihnen?', 1),
('What is your name?', 'Wie heißen Sie?', 1),
('Where are you from?', 'Woher kommen Sie?', 1),
('I like to travel.', 'Ich reise gerne.', 1),
('I am learning German.', 'Ich lerne Deutsch.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(166, 25), (167, 25), (168, 25), (169, 25), (170, 25);

-- Deck 26
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Computer Science Fundamentals', 'Learn the fundamentals of computer science.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is a computer?', 'An electronic device for storing and processing data.', 1),
('Define algorithm.', 'A set of instructions designed to perform a specific task.', 1),
('What is programming?', 'The process of creating instructions that tell a computer how to perform a task.', 1),
('Explain binary code.', 'The most basic language of computers, representing data in 0s and 1s.', 1),
('What is a database?', 'An organized collection of data, generally stored electronically.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(171, 26), (172, 26), (173, 26), (174, 26), (175, 26);

-- Deck 27
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Human Anatomy - Body Parts', 'Study and learn about different body parts.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Heart', 'A muscular organ that pumps blood through the body.', 1),
('Brain', 'The organ of the body in the head that controls functions, movements, sensations, and thoughts.', 1),
('Lungs', 'Pair of breathing organs that process the air we inhale.', 1),
('Liver', 'A large organ that processes nutrients and filters blood.', 1),
('Kidneys', 'Organs that filter waste from the blood and produce urine.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(176, 27), (177, 27), (178, 27), (179, 27), (180, 27);

-- Deck 28
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic Medical Terminology', 'Learn basic terms used in the medical field.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hypertension', 'A condition in which the blood pressure is persistently elevated.', 1),
('Diabetes', 'A disease that occurs when blood glucose is too high.', 1),
('Antibiotics', 'Medicines used to treat infections caused by bacteria.', 1),
('Vaccine', 'A substance that stimulates the body’s immune response against diseases.', 1),
('Anesthesia', 'Medically induced insensitivity to pain.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(181, 28), (182, 28), (183, 28), (184, 28), (185, 28);

-- Deck 29
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Introduction to Programming', 'Basics of programming for beginners.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Variable', 'A storage location paired with an associated name, which contains some known or unknown quantity.', 1),
('Function', 'A piece of code that can be called by name and may return a value.', 1),
('Loop', 'A programming structure that repeats a sequence of instructions.', 1),
('Conditional Statement', 'A feature of a programming language, which performs different computations based on a boolean condition.', 1),
('Array', 'A data structure consisting of a collection of elements, each identified by an index.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(186, 29), (187, 29), (188, 29), (189, 29), (190, 29);

-- Deck 30
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Medical Staff Roles', 'Learn about different roles of medical staff.', 1);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Doctor', 'A qualified practitioner of medicine; a physician.', 1),
('Nurse', 'A person trained to care for the sick or infirm.', 1),
('Surgeon', 'A medical doctor who performs operations.', 1),
('Pharmacist', 'A person trained to prepare and dispense medicinal drugs.', 1),
('Paramedic', 'A person trained to give emergency medical care.', 1);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(191, 30), (192, 30), (193, 30), (194, 30), (195, 30);