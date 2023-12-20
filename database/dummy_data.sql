-- Deck 1: Basic Chemistry
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basic Chemistry', 'Introduction to fundamental concepts of chemistry.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is the atomic number?', 'Number of protons in the nucleus of an atom.', 0),
('Define covalent bond.', 'A chemical bond formed by the sharing of electron pairs between atoms.', 0),
('What is Avogadro’s number?', '6.022 x 10^23 particles/mole, represents the number of particles in one mole of a substance.', 0),
('Define molarity.', 'The concentration of a solution expressed as the number of moles of solute per liter of solution.', 0),
('What is the pH scale?', 'A scale used to specify the acidity or basicity of an aqueous solution.', 0),
('Define a catalyst.', 'A substance that speeds up a chemical reaction without being consumed.', 0),
('What are isotopes?', 'Atoms of the same element with different numbers of neutrons.', 0),
('Define electrolysis.', 'The process of using electricity to drive a non-spontaneous chemical reaction.', 0),
('What is the ideal gas law?', 'PV = nRT, where P is pressure, V is volume, n is moles of gas, R is the gas constant, and T is temperature.', 0),
('What is a buffer solution?', 'A solution that can resist changes in pH upon the addition of an acid or a base.', 0);

-- Linking cards to Deck 1 (Basic Chemistry)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1);

-- Deck 2: Introduction to Programming
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Programming', 'Fundamentals of programming using Python.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is a variable in programming?', 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.', 0),
('Define a function in Python.', 'A block of code which only runs when it is called. It can pass data, known as parameters, into a function.', 0),
('What is a loop in programming?', 'A sequence of instructions that is continually repeated until a certain condition is reached.', 0),
('Explain the concept of an algorithm.', 'A step-by-step procedure for solving a problem or accomplishing some end.', 0),
('What is a conditional statement in Python?', 'Used to perform different actions based on different conditions, e.g., if, elif, else.', 0),
('Define object-oriented programming.', 'A programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields, and code, in the form of procedures.', 0),
('What is an exception in Python?', 'An error that occurs during the execution of a program. Python uses try... except blocks to handle exceptions.', 0),
('What does "for" loop do in Python?', 'Iterates over a sequence (like a list, tuple, dictionary, set, or string) and executes code for each item.', 0),
('What is a class in Python?', 'A blueprint for creating objects (a particular data structure), providing initial values for state (member variables) and implementations of behavior (member functions, methods).', 0),
('Explain the concept of inheritance in programming.', 'A mechanism where a new class is derived from an existing class. The new class is called derived (or child) class, and the one from which it inherits is called the base (or parent) class.', 0);

-- Linking cards to Deck 2 (Introduction to Programming)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (18, 2), (19, 2), (20, 2);

-- Deck 3: World History Overview
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('World History Overview', 'A brief overview of major events in world history.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What was the Renaissance?', 'A period in European history marking the transition from the Middle Ages to modernity, characterized by an emphasis on classical culture, humanism, and a surge in artistic, cultural, and intellectual development.', 0),
('Who was Alexander the Great?', 'An ancient Macedonian ruler known for creating one of the largest empires in the ancient world by the age of 30.', 0),
('What caused World War I?', 'A complex series of events, but it is generally believed that the immediate cause was the assassination of Archduke Franz Ferdinand of Austria-Hungary.', 0),
('What was the Industrial Revolution?', 'A period of major industrialization from the late 1700s to the early 1800s which saw the introduction of machinery, predominantly in Europe and North America.', 0),
('What was the significance of the French Revolution?', 'It brought down the French monarchy, established a republic, catalyzed violent periods of political turmoil, and finally culminated in a dictatorship under Napoleon.', 0),
('Describe the Cold War.', 'A period of geopolitical tension between the Soviet Union and the United States and their respective allies, the Eastern Bloc and the Western Bloc, after World War II.', 0),
('What was the Silk Road?', 'An ancient network of trade routes connecting the East and West, important for cultural, commercial, and technological exchange.', 0),
('Who was Genghis Khan?', 'The founder and first Great Khan of the Mongol Empire, which became the largest contiguous empire in history after his death.', 0),
('What was the significance of the Magna Carta?', 'A charter of rights agreed to by King John of England in 1215, widely seen as an early step in the development of constitutional government.', 0),
('Explain the impact of the discovery of the New World.', 'It led to the exchange of goods and ideas between the Americas and the Old World and had a profound impact on the history of the world, particularly regarding colonization and trade.', 0);

-- Linking cards to Deck 3 (World History Overview)
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(21, 3), (22, 3), (23, 3), (24, 3), (25, 3), (26, 3), (27, 3), (28, 3), (29, 3), (30, 3);

-- Deck 4: Basic Economics
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basic Economics', 'Fundamental concepts in economics.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Define ''Economics''.', 'The study of how societies use scarce resources to produce valuable commodities and distribute them among different people.', 0),
('What is "GDP"?', 'Gross Domestic Product, the total value of goods produced and services provided in a country during one year.', 0),
('Explain "Inflation".', 'The rate at which the general level of prices for goods and services is rising, and, subsequently, purchasing power is falling.', 0),
('What is "Supply and Demand"?', "A model of price determination in a market, prices are determined by the relationship between supply and demand.", 0),
('Define "Monopoly".', 'A market structure characterized by a single seller, selling a unique product in the market.', 0),
('What is "Fiscal Policy"?', "Government adjustments to its spending levels and tax rates to monitor and influence a nation's economy.", 0),
('Explain "Macroeconomics".', 'The part of economics concerned with large-scale or general economic factors, such as interest rates and national productivity.', 0),
('What is "Microeconomics"?', 'The part of economics concerned with single factors and the effects of individual decisions.', 0),
('Define "Opportunity Cost".', 'The loss of potential gain from other alternatives when one alternative is chosen.', 0),
('What is "Elasticity" in economics?', 'A measure of how much buyers and sellers respond to changes in market conditions.', 0);

-- Linking Cards to Deck 4: Basic Economics
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(31, 4), (32, 4), (33, 4), (34, 4), (35, 4), 
(36, 4), (37, 4), (38, 4), (39, 4), (40, 4);

-- Deck 5: Advanced Mathematics
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Advanced Mathematics', 'Complex mathematical theories and applications.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Define "Integral Calculus".', 'The study of the accumulation of quantities, such as areas under a curve, and their properties.', 0),
('What is "Differential Calculus"?', 'The study of rates at which quantities change.', 0),
('Explain "Linear Algebra".', 'The branch of mathematics concerning linear equations, linear functions, and their representations in vector spaces and through matrices.', 0),
('What is a "Matrix" in mathematics?', 'A rectangular array of numbers, symbols, or expressions, arranged in rows and columns.', 0),
('Define "Vector Space".', 'A collection of objects called vectors, which may be added together and multiplied by numbers, called scalars.', 0),
('Explain "Complex Numbers".', 'Numbers that consist of a real and an imaginary part and are written in the form a + bi.', 0),
('What is "Fourier Transform"?', 'A mathematical transform that decomposes functions depending on space or time into functions depending on spatial or temporal frequency.', 0),
('Define "Topology".', 'The mathematical study of shapes and topological spaces.', 0),
('What is "Set Theory"?', 'The branch of mathematical logic that studies sets, which are collections of objects.', 0),
('Explain "Probability Theory".', 'The branch of mathematics concerned with probability, the analysis of random phenomena.', 0);

-- Linking Cards to Deck 5: Advanced Mathematics
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(41, 5), (42, 5), (43, 5), (44, 5), (45, 5), 
(46, 5), (47, 5), (48, 5), (49, 5), (50, 5);

-- Deck 6: Introduction to Philosophy
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Philosophy', 'Exploring fundamental philosophical questions and thinkers.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Philosophy"?', 'The study of general and fundamental questions, such as those about existence, reason, knowledge, values, and language.', 0),
('Who was Socrates?', 'A classical Greek philosopher credited as one of the founders of Western philosophy.', 0),
('Define "Existentialism".', 'A philosophical theory or approach that emphasizes individual existence, freedom, and choice.', 0),
('What did Plato write about?', 'Plato was a student of Socrates and wrote on a wide range of topics including political philosophy, ethics, and metaphysics.', 0),
('Who was Friedrich Nietzsche?', 'A German philosopher who wrote critically about religion, morality, culture, philosophy, and science.', 0),
('Define "Utilitarianism".', 'The doctrine that actions are right if they are useful or for the benefit of a majority.', 0),
('Explain "Epistemology".', 'The branch of philosophy concerned with the theory of knowledge.', 0),
('What is "Metaphysics"?', 'A branch of philosophy that explores the fundamental nature of reality.', 0),
('Who was Immanuel Kant?', 'A German philosopher who is a central figure in modern philosophy, known for his works in epistemology, ethics, and metaphysics.', 0),
('Define "Aesthetics".', 'The branch of philosophy dealing with the nature of beauty, art, and taste, with the creation and appreciation of beauty.', 0);

-- Linking Cards to Deck 6: Introduction to Philosophy
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(51, 6), (52, 6), (53, 6), (54, 6), (55, 6), 
(56, 6), (57, 6), (58, 6), (59, 6), (60, 6);


-- Deck 7: Introduction to Computer Science
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Introduction to Computer Science', 'Foundational concepts in computer science and programming.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Computer Science"?', 'The study of both computer hardware and software design, encompassing theoretical algorithms and the practical problems of implementing them.', 0),
('Define "Algorithm".', 'A set of instructions designed to perform a specific task.', 0),
('Explain "Machine Learning".', 'A branch of artificial intelligence based on the idea that systems can learn from data, identify patterns, and make decisions with minimal human intervention.', 0),
('What is "Object-Oriented Programming"?', 'A programming paradigm based on the concept of "objects", which can contain data and code: data in the form of fields, and code, in the form of procedures.', 0),
('Define "Database".', 'An organized collection of data, generally stored and accessed electronically from a computer system.', 0),
('What is "Artificial Intelligence"?', 'The simulation of human intelligence in machines that are programmed to think and learn like humans.', 0),
('Explain "Operating System".', 'System software that manages computer hardware, software resources, and provides common services for computer programs.', 0),
('What is "Big Data"?', 'Extremely large data sets that may be analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions.', 0),
('Define "Network Security".', 'The practice of preventing and protecting against unauthorized intrusion into corporate networks.', 0),
('Explain "Blockchain Technology".', 'A decentralized, distributed ledger technology that records the provenance of a digital asset.', 0);

-- Linking Cards to Deck 7: Introduction to Computer Science
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(61, 7), (62, 7), (63, 7), (64, 7), (65, 7), 
(66, 7), (67, 7), (68, 7), (69, 7), (70, 7);

-- Deck 8: Basics of Psychology
INSERT INTO "decks" ("name", "description", "creator_id") VALUES ('Basics of Psychology', 'An introduction to psychological theories and practices.', 0);
INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is "Psychology"?', 'The scientific study of the mind and behavior.', 0),
('Define "Behaviorism".', 'A theory of learning based on the idea that all behaviors are acquired through conditioning.', 0),
('Explain "Cognitive Psychology".', 'The study of mental processes such as "attention, language use, memory, perception, problem-solving, creativity, and thinking."', 0),
('What is "Psychoanalysis"?', 'A set of psychological and psychotherapeutic theories and associated techniques, originally popularized by Austrian neurologist Sigmund Freud.', 0),
('Define "Humanistic Psychology".', 'A perspective that emphasizes looking at the whole individual and stresses concepts such as free will, self-efficacy, and self-actualization.', 0),
('What is "Developmental Psychology"?', 'The scientific study of how and why human beings change over the course of their life.', 0),
("Explain 'Social Psychology'.", "The scientific study of how people's thoughts, feelings, and behaviors are influenced by the actual, imagined, or implied presence of others.", 0),
('What is "Neuropsychology"?', 'The study of the relationship between behavior, emotion, and cognition on the one hand, and brain function on the other.', 0),
('Define "Forensic Psychology".', 'The intersection between psychology and the justice system. It involves understanding fundamental legal principles, particularly with regard to expert witness testimony and the specific content area of concern.', 0),
('Explain "Positive Psychology".', 'The study of "positive subjective experience, positive individual traits, and positive institutions" and it promises to improve quality of life.', 0);

-- Linking Cards to Deck 8: Basics of Psychology
INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(71, 8), (72, 8), (73, 8), (74, 8), (75, 8), 
(76, 8), (77, 8), (78, 8), (79, 8), (80, 8);

-- Deck 9
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to French Translation', 'Deck for translating common English phrases and words into French.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Bonjour', 0),
('Goodbye', 'Au revoir', 0),
('Please', "S'il vous plaît", 0),
('Thank you', 'Merci', 0),
('Yes', 'Oui', 0),
('No', 'Non', 0),
('How are you?', 'Comment ça va?', 0),
('I am fine', 'Je vais bien', 0),
('What is your name?', 'Comment vous appelez-vous?', 0),
('My name is...', "Je m'appelle...", 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(81, 9), (82, 9), (83, 9), (84, 9), (85, 9), 
(86, 9), (87, 9), (88, 9), (89, 9), (90, 9);

-- Deck 10
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to French - Fruits', 'Translate fruit names from English to French.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Apple', 'Pomme', 0),
('Banana', 'Banane', 0),
('Grape', 'Raisin', 0),
('Orange', 'Orange', 0),
('Pineapple', 'Ananas', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(91, 10), (92, 10), (93, 10), (94, 10), (95, 10);

-- Deck 11
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('French to English - Fruits', 'Translate fruit names from French to English.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Pomme', 'Apple', 0),
('Banane', 'Banana', 0),
('Raisin', 'Grape', 0),
('Orange', 'Orange', 0),
('Ananas', 'Pineapple', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(96, 11), (97, 11), (98, 11), (99, 11), (100, 11);

-- Deck 12
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Spanish to English - Fruits', 'Translate fruit names from Spanish to English.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Manzana', 'Apple', 0),
('Plátano', 'Banana', 0),
('Uva', 'Grape', 0),
('Naranja', 'Orange', 0),
('Piña', 'Pineapple', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(101, 12), (102, 12), (103, 12), (104, 12), (105, 12);

-- Deck 13
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('English to English - Fruits', 'Learn synonyms or descriptions of fruits in English.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Apple', 'A round fruit with red, yellow, or green skin.', 0),
('Banana', 'A long curved yellow fruit.', 0),
('Grape', 'A small juicy fruit, typically purple or green.', 0),
('Orange', 'A citrus fruit with a tough bright orange skin.', 0),
('Pineapple', 'A tropical fruit with a rough green or brown skin.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(111, 13), (112, 13), (113, 13), (114, 13), (115, 13);

-- Deck 14
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Learning Verbs in English', 'Study and learn common English verbs.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Run', 'Move at a speed faster than a walk.', 0),
('Jump', 'Push oneself off a surface into the air by using the muscles in one’s legs.', 0),
('Read', 'Look at and comprehend the meaning of written or printed matter.', 0),
('Write', 'Mark coherent words on paper.', 0),
('Speak', 'Talk: use vocal sounds to express thoughts or feelings.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(111, 14), (112, 14), (113, 14), (114, 14), (115, 14);

-- Deck 15
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Fill in the Blank - Single Word', 'Complete the sentence by filling in a single word.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('An apple a day keeps the ___ away.', 'doctor', 0),
('Better late than ___ .', 'never', 0),
('Actions speak louder than ___ .', 'words', 0),
('The early bird catches the ___ .', 'worm', 0),
('A picture is worth a thousand ___ .', 'words', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(116, 15), (117, 15), (118, 15), (119, 15), (120, 15);

-- Deck 16
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic German Vocabulary', 'Learn basic German vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Hallo', 0),
('Goodbye', 'Auf Wiedersehen', 0),
('Thank you', 'Danke', 0),
('Yes', 'Ja', 0),
('No', 'Nein', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(121, 16), (122, 16), (123, 16), (124, 16), (125, 16);

-- Deck 17
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic Spanish Vocabulary', 'Learn basic Spanish vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Hola', 0),
('Goodbye', 'Adiós', 0),
('Thank you', 'Gracias', 0),
('Yes', 'Sí', 0),
('No', 'No', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(126, 17), (127, 17), (128, 17), (129, 17), (130, 17);

-- Deck 18
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic French Vocabulary', 'Learn basic French vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hello', 'Bonjour', 0),
('Goodbye', 'Au revoir', 0),
('Thank you', 'Merci', 0),
('Yes', 'Oui', 0),
('No', 'Non', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(131, 18), (132, 18), (133, 18), (134, 18), (135, 18);

-- Deck 19
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced German Vocabulary', 'Learn advanced German vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Freiheit', 0),
('Experience', 'Erfahrung', 0),
('Knowledge', 'Wissen', 0),
('Strength', 'Stärke', 0),
('Happiness', 'Glück', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(136, 19), (137, 19), (138, 19), (139, 19), (140, 19);

-- Deck 20
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('German Phrases for Travelers', 'Essential phrases for travelers in German.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', 'Wo ist die Toilette?', 0),
('How much does this cost?', 'Wie viel kostet das?', 0),
('Can you help me?', 'Können Sie mir helfen?', 0),
('I would like a coffee.', 'Ich möchte einen Kaffee.', 0),
('I do not understand.', 'Ich verstehe nicht.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(141, 20), (142, 20), (143, 20), (144, 20), (145, 20);

-- Deck 21
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced Spanish Vocabulary', 'Learn advanced Spanish vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Libertad', 0),
('Experience', 'Experiencia', 0),
('Knowledge', 'Conocimiento', 0),
('Strength', 'Fuerza', 0),
('Happiness', 'Felicidad', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(146, 21), (147, 21), (148, 21), (149, 21), (150, 21);

-- Deck 22
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Spanish Phrases for Travelers', 'Essential phrases for travelers in Spanish.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', '¿Dónde está el baño?', 0),
('How much does this cost?', '¿Cuánto cuesta esto?', 0),
('Can you help me?', '¿Puede ayudarme?', 0),
('I would like a coffee.', 'Me gustaría un café.', 0),
('I do not understand.', 'No entiendo.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(151, 22), (152, 22), (153, 22), (154, 22), (155, 22);

-- Deck 23
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Advanced French Vocabulary', 'Learn advanced French vocabulary words.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Freedom', 'Liberté', 0),
('Experience', 'Expérience', 0),
('Knowledge', 'Connaissance', 0),
('Strength', 'Force', 0),
('Happiness', 'Bonheur', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(156, 23), (157, 23), (158, 23), (159, 23), (160, 23);

-- Deck 24
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('French Phrases for Travelers', 'Essential phrases for travelers in French.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Where is the bathroom?', 'Où sont les toilettes?', 0),
('How much does this cost?', 'Combien cela coûte-t-il?', 0),
('Can you help me?', 'Pouvez-vous m’aider?', 0),
('I would like a coffee.', 'Je voudrais un café.', 0),
('I do not understand.', 'Je ne comprends pas.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(161, 24), (162, 24), (163, 24), (164, 24), (165, 24);

-- Deck 25
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('German Conversation Practice', 'Practice conversational phrases in German.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('How are you?', 'Wie geht es Ihnen?', 0),
('What is your name?', 'Wie heißen Sie?', 0),
('Where are you from?', 'Woher kommen Sie?', 0),
('I like to travel.', 'Ich reise gerne.', 0),
('I am learning German.', 'Ich lerne Deutsch.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(166, 25), (167, 25), (168, 25), (169, 25), (170, 25);

-- Deck 26
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Computer Science Fundamentals', 'Learn the fundamentals of computer science.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is a computer?', 'An electronic device for storing and processing data.', 0),
('Define algorithm.', 'A set of instructions designed to perform a specific task.', 0),
('What is programming?', 'The process of creating instructions that tell a computer how to perform a task.', 0),
('Explain binary code.', 'The most basic language of computers, representing data in 0s and 1s.', 0),
('What is a database?', 'An organized collection of data, generally stored electronically.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(171, 26), (172, 26), (173, 26), (174, 26), (175, 26);

-- Deck 27
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Human Anatomy - Body Parts', 'Study and learn about different body parts.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Heart', 'A muscular organ that pumps blood through the body.', 0),
('Brain', 'The organ of the body in the head that controls functions, movements, sensations, and thoughts.', 0),
('Lungs', 'Pair of breathing organs that process the air we inhale.', 0),
('Liver', 'A large organ that processes nutrients and filters blood.', 0),
('Kidneys', 'Organs that filter waste from the blood and produce urine.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(176, 27), (177, 27), (178, 27), (179, 27), (180, 27);

-- Deck 28
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Basic Medical Terminology', 'Learn basic terms used in the medical field.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Hypertension', 'A condition in which the blood pressure is persistently elevated.', 0),
('Diabetes', 'A disease that occurs when blood glucose is too high.', 0),
('Antibiotics', 'Medicines used to treat infections caused by bacteria.', 0),
('Vaccine', 'A substance that stimulates the body’s immune response against diseases.', 0),
('Anesthesia', 'Medically induced insensitivity to pain.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(181, 28), (182, 28), (183, 28), (184, 28), (185, 28);

-- Deck 29: World Geography Basics
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('World Geography Basics', 'Basics of world geography including countries, capitals, and geographical features.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('What is the capital of France?', 'Paris', 0),
('What continent is Brazil in?', 'South America', 0),
('Which is the longest river in the world?', 'The Nile River', 0),
('What is the largest ocean?', 'The Pacific Ocean', 0),
('Which country has the most population?', 'China', 0),
('What is the smallest country in the world?', 'Vatican City', 0),
('Which desert is the largest in the world?', 'The Sahara Desert', 0),
('What mountain is the highest above sea level?', 'Mount Everest', 0),
('Which forest is known as the lungs of the Earth?', 'The Amazon Rainforest', 0),
('Which country is both in Asia and Europe?', 'Turkey', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(186, 29), (187, 29), (188, 29), (189, 29), (190, 29),
(191, 29), (192, 29), (193, 29), (194, 29), (195, 29);


-- Deck 30
INSERT INTO "decks" ("name", "description", "creator_id") VALUES 
('Medical Staff Roles', 'Learn about different roles of medical staff.', 0);

INSERT INTO "cards" ("front_side", "back_side", "creator_id") VALUES 
('Doctor', 'A qualified practitioner of medicine, a physician.', 0),
('Nurse', 'A person trained to care for the sick or infirm.', 0),
('Surgeon', 'A medical doctor who performs operations.', 0),
('Pharmacist', 'A person trained to prepare and dispense medicinal drugs.', 0),
('Paramedic', 'A person trained to give emergency medical care.', 0);

INSERT INTO "card_links" ("card_id", "deck_id") VALUES 
(196, 30), (197, 30), (198, 30), (199, 30), (200, 30);
