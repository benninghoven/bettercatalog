#CPSC 362 PROJECT
DROP DATABASE IF EXISTS COURSECATALOG;
CREATE DATABASE COURSECATALOG;

USE COURSECATALOG;

CREATE TABLE IF NOT EXISTS COURSE( 
DEPTCODE			CHAR(4) NOT NULL,
COURSENUM			SMALLINT NOT NULL,
COURSELETTER		CHAR,
COURSENAME			VARCHAR(100) NOT NULL,
COURSEDESCRIPTION	VARCHAR(500),
CREDITS				TINYINT NOT NULL,
GRADCREDIT			BOOL,
MAJMINREQ			BOOL,
PRIMARY KEY (DEPTCODE, COURSENUM, COURSELETTER)
#OLD PK IS DEPTCODE, COURSENUM, COURSELETTER
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS COURSEPREREQ(
COURSEDEPT			CHAR(4) NOT NULL,
COURSENUM			SMALLINT NOT NULL,
COURSELETTER		CHAR NOT NULL,
PREREQDEPT			CHAR(4) NOT NULL,
PREREQNUM			SMALLINT NOT NULL,
PREREQCOURSELETTER	CHAR NOT NULL,
ISCOREQ				BOOLEAN,
CONSTRAINT FKCoursePreReq
	FOREIGN KEY (COURSEDEPT, COURSENUM, COURSELETTER) REFERENCES COURSE (DEPTCODE, COURSENUM, COURSELETTER)
)ENGINE = INNODB;

-- CREATE TABLE COREQUISITE(
-- COURSEDEPT			CHAR(4) NOT NULL,
-- COURSENUM			SMALLINT NOT NULL,
-- COURSELETTER		CHAR NOT NULL,
-- COREQDEPT			CHAR(4) NOT NULL,
-- COREQNUM			SMALLINT NOT NULL,
-- COREQCOURSELETTER	CHAR,
-- FOREIGN KEY (COURSEDEPT) REFERENCES COURSE (DEPTCODE),
-- FOREIGN KEY (COURSENUM) REFERENCES COURSE (COURSENUM),
-- FOREIGN KEY (COURSELETTER) REFERENCES COURSE (COURSELETTER)
-- );

#SECONDARY INDEX FOR COURSE SINCE THE PRIMARY INDEX IS THE INNODB OR COURSEID (CLUSTERED)
CREATE INDEX COURSEHEADER ON COURSE (DEPTCODE, COURSENUM, COURSELETTER);

SHOW FULL COLUMNS FROM COURSEPREREQ;

SELECT * FROM COURSE;

INSERT INTO COURSE (DEPTCODE, COURSENUM, COURSELETTER, COURSENAME, COURSEDESCRIPTION, CREDITS, GRADCREDIT, MAJMINREQ) VALUES
('CPSC', 120, '', 'Introduction to Programming', 'Introduction to the concepts underlying all computer programming: design and execution of programs; sequential nature of programs; use of assignment, control and input/output statements to accomplish desired tasks; design and use of functions. Structured and object-oriented methodologies. (1.5 hours lecture, 3 hours laboratory)', 3, False, TRUE),
('CPSC', 121, '', 'Object-Oriented Programming', 'The object-oriented programming paradigm: classes, member functions, interfaces, inheritance, polymorphism, and exceptions. Design practices including encapsulation, decoupling, and documentation. Pointers/references and memory management. Recursion. (2 hours lecture, 2 hours activity)', 3, False, TRUE),
('CPSC', 131, '', 'Data Structures', 'Classical data structures: vector, linked list, stack, queue, binary search tree, and graph representations. Worst-case analysis, amortized analysis, and big-O notation. Object-oriented and recursive implementation of data structures. Self-resizing vectors and self-balancing trees. Empirical performance measurement.', 3, False, TRUE),
('CPSC', 223, 'C', 'C Programming', 'Systems programming in the C language, including its syntax and semantics; essential idioms; important parts of the C11 and POSIX C APIs; security issues; and notable extensions libraries.', 3, False, TRUE),
('CPSC', 223, 'J', 'Java Programming', 'Characteristics of Java: portable, robust, secure, object-oriented, high performance; using the Java environment; server administration; types, expressions and control flow; classes, interfaces and packages; threads; exceptions; class libraries; Java for the Internet; tools, the Java Virtual machine. (2 hours lecture, 2 hours lab per week)', 3, False, TRUE),
('CPSC', 223, 'N', 'Visual C# Programming', 'Characteristics of C#, object-oriented design concepts, control structures, methods, arrays, classes, objects, inheritance, polymorphism, exception handling, graphical user interfaces, multithreading, characters, strings, files, streams. Rudiments of the Unified Modeling Language Software development assignments. (2 hours lecture, 2 hours laboratory)', 3, False, TRUE),
('CPSC', 223, 'P', 'Python Programming', 'Characteristics of Python: portable, robust, secure, object-oriented, functional, high performance, extensible; types, expressions, and control flow; classes, abstract base classes, modules, and packages; threads; exceptions; Python standard library. 2 hours lecture and 2 hours laboratory per week)', 3, False, TRUE),
('CPSC', 240, '', 'Computer Organization and Assembly Language', 'Digital logic and architecture of a computer system, machine level representation of data, memory system organization, structure of low-level computer languages. Machine, assembly, and macro language programming. Principles of assembler operation, input-output programming, interrupt/exception handling. Laboratory programming assignments. (2 hours lecture, 2 hours laboratory)', 3, False, TRUE),
('CPSC', 253, '', 'Cybersecurity Foundations and Principles', 'Security goals, security systems, access controls, networks and security, integrity, cryptography fundamentals, authentication. Attacks: software, network, website; management considerations, security standards in government and industry; security issues in requirements, architecture, design, implementation, testing, operation, maintenance, acquisition and services.', 3, False, TRUE),
('CPSC', 315, '', 'Professional Ethics in Computing', 'Ethics and moral philosophy as applied to software and digital artifacts. Notions of rights, responsibilities, property, ownership, privacy, security, and professional ethics. Security obligations. Intellectual propertystatutes, licenses, and their terms. Oral and written reports are required.', 3, False, TRUE),
('CPSC', 323, '', 'Compilers and Languages', 'Basic concepts of programming languages and principles of translation. Topics include history of programming languages, various programming paradigms, language design issues and criteria, design of compilers for modern programming languages.', 3, False, TRUE),
('CPSC', 332, '', 'File Structures and Database Systems', 'Fundamental theories and design of database systems, the Structured Query Language (SQL), basic concepts and techniques of data organization in secondary storage. Topics include introduction to database systems, ER model, relational model, index structures and hashing techniques.', 3, False, TRUE),
('CPSC', 335, '', 'Algorithm Engineering', 'Algorithm design using classical patterns: exhaustive search, divide and conquer, randomization, hashing, reduction, dynamic programming, and the greedy method. Asymptotic and experimental efficiency analysis. NP-completeness and decidability. Implementing algorithms to solve practical problems.', 3, False, TRUE),
('CPSC', 351, '', 'Operating Systems Concepts', 'Resource management, memory organization, input/output, control process synchronization and other concepts as related to the objectives of multi-user operating systems.', 3, False, TRUE),
('CPSC', 362, '', 'Foundations of Software Engineering', 'Basic concepts, principles, methods, techniques and practices of software engineering. All aspects of the software engineering fields. Use Computer-Aided Software Engineering (CASE) tools.', 3, False, TRUE),
('CPSC', 471, '', 'Computer Communications', 'Introduction to digital data communications. Terminology, networks and their components, common-carrier services, telecommunication facilities, terminals, error control, multiplexing and concentration techniques.', 3, True, TRUE),
('CPSC', 481, '', 'Artificial Intelligence', 'Using computers to simulate human intelligence. Production systems, pattern recognition, problem solving, searching game trees, knowledge representation and logical reasoning. Programming in AI environments.', 3, True, TRUE),
('CPSC', 490, '', 'Undergraduate Seminar in Computer Science', 'Review of foundational computer science theories and principles, real-world application development methods and processes, and industry practices. Survey of modern computing technologies. Research methods. Identification of research or practical application problems. Writing and presenting a proposal for a capstone project.', 3, False, TRUE),
('CPSC', 491, '', 'Senior Capstone Project in Computer Science', 'A computer science research or real-world level of application development project. Business communication. Presenting the results to a wide range of audiences. Demonstrating the culminating experience of the practicum in computer science. Writing a final project report and technical documents such as user manuals, installation guides, feasibility study reports.', 3, False, TRUE),
('MATH', 150, 'A', 'Calculus I', 'Properties of functions. The limit, derivative and definite integral concepts; applications of the derivative, techniques and applications of integration. Six units of credit are given for both MATH 130 and MATH 150A, or for both MATH 135 and MATH 150A. Biology, geology and earth science majors who pass ALEKS must take MATH 130. CBE majors who pass ALEKS must take MATH 135.', 4, False, TRUE),
('MATH', 150, 'B', 'Calculus II', 'Techniques of integration, improper integrals and applications of integration. Introduction to differential equations. Parametric equations, sequences and series.', 4, False, TRUE),
('MATH', 170, 'A', 'Mathematical Structures I', 'First of two semesters of fundamental discrete mathematical concepts and techniques needed in computer-related disciplines. Logic, truth tables, elementary set theory, proof techniques, combinatorics, Boolean algebra, recursion and graph theory. Must have completed four years of high school mathematics.', 3, False, TRUE),
('MATH', 170, 'B', 'Mathematical Structures II', 'Second of two semesters of fundamental discrete mathematical concepts and techniques needed in computer-related disciplines, focusing on linear algebra.', 3, False, TRUE),
('MATH', 338, '', 'Statistics Applied to Natural Sciences', 'Introduction to the theory and application of statistics. Elementary probability, estimation, hypothesis testing, regression, variance analysis, non-parametric tests. Computer-aided analysis of real data. Graphical techniques, generating and interpreting statistical output, presentation of analysis.', 4, False, TRUE),
('BIOL', 101, '', 'Elements of Biology', 'Underlying principles governing life forms, processes and interactions. Elements of biology and reasoning skills for understanding scientific issues on personal, societal and global levels. For non-science majors. No credit toward biological science major.', 3, False, TRUE),
('BIOL', 101, 'L', 'Elements of Biology Laboratory', 'Laboratory experiments demonstrating principles from the lecture course. Scientific inquiry, cells, physiology, genetics, biodiversity, evolution and ecology. Hybrid sections require online and in-person activities (3 hours laboratory or fieldwork; weekend field trips and online coursework may be required). For non-science majors.', 1, False, TRUE),
('BIOL', 151, '', 'Cellular and Molecular Biology', 'Lecture and laboratory exploration of eukaryotic/prokaryotic cellular structure and function, biological molecules, classical/Mendelian genetics, regulation of gene expression and biotechnology, cell signaling, metabolic pathways, the process and regulation of cellular reproduction, evolution of multicellularity. (For majors in CNSM). (3 hours lecture, 3 hours laboratory)', 4, False, TRUE),
('BIOL', 152, '', 'Evolution and Organismal Biology', 'Introduction to evolution and organismal biology. Evolutionary processes that resulted in the biodiversity of life on Earth. Physiological processes and ecological challenges for organisms. (3 hours lecture, 3 hours laboratory/fieldwork; weekend field trips required)', 4, False, TRUE),
('CHEM', 120, 'A', 'General Chemistry', 'For majors and minors in the physical and biological sciences. The principles of chemistry: stoichiometry, acids, bases, redox reactions, gas laws, solid and liquid states, changes of state, modern atomic concepts, periodicity and chemical bonding. Laboratory: elementary syntheses, spectroscopy and volumetric quantitative analysis. (3 hours lecture, 3 hours laboratory, 2 hours activity)', 5, False, TRUE),
('CHEM', 120, 'B', 'General Chemistry', 'For majors and minors in the physical and biological sciences, chemical thermodynamics, chemical equilibrium (gaseous, aqueous, acid-base, solubility and complexation), elementary electrochemistry and chemical kinetics. Laboratory: quantitative and qualitative analysis and elementary physical chemistry; some qualitative analysis. (3 hours lecture, 6 hours laboratory).', 5, False, TRUE),
('CHEM', 123, '', 'Chemistry for Engineers', 'Fundamental concepts of chemistry for engineering students. Atomic structure, periodic table, stoichiometry, states of matter, chemical bonding, new materials, solutions, thermodynamics, reaction rates, equilibrium, electrochemistry, polymers and nuclear reactions.', 3, False, TRUE),
('CHEM', 125, '', 'General Chemistry B Lecture', 'For students who do not need a second semester of general chemistry lab. Chemical thermodynamics, chemical equilibrium (gaseous, aqueous, acid-base, solubility and complexion), elementary electrochemistry and chemical kinetics. Not open to students with credit in CHEM 120B.', 3, False, TRUE),
('GEOL', 101, '', 'Introduction to Geology', 'Introduction to the science of rocks, fossils, volcanoes, earthquakes, landscapes and oceans. Natural hazards, geology in everyday life and geology as field of practice. High school algebra recommended.', 3, False, TRUE),
('GEOL', 101, 'L', 'Introduction to Geology Laboratory', 'Hands-on analysis and evaluation of rocks, maps, geologic time and Earth processes. Natural hazards, geology in everyday life and scientific inquiry.', 1, False, TRUE),
('GEOL', 201, '', 'Earth History', 'Evolution of Earth as interpreted from rocks, fossils and geologic structures. Plate tectonics provides a unifying theme for consideration of mountain building, evolution of life and ancient environments. (2 hours lecture, 3 hours laboratory, field trips)', 3, False, TRUE),
('GEOL', 201, 'L', 'Earth History Supplemental Lab', 'Supervised research on topics related to Earth history. Project will result in a term paper and/or web page. (3 hours laboratory, field trips)', 1, False, TRUE),
('MATH', 250, 'A', 'Calculus III', 'Calculus of functions of several variables. Partial derivatives and multiple integrals with applications. Parametric curves, vector-valued functions, vector fields, line integrals, Green’s Theorem, Stokes’ theorem, the Divergence Theorem, vectors and the geometry of 3-space.', 4, False, TRUE),
('MATH', 250, 'B', 'Introduction to Linear Algebra and Differential Equations', 'Introduction to the solutions of ordinary differential equations and their relationship to linear algebra. Topics include matrix algebra, systems of linear equations, vector spaces, linear independence, linear transformations and eigenvalues.', 4, False, TRUE),
('PHYS', 225, '', 'Fundamental Physics: Mechanics', 'Classical Newtonian mechanics; linear and circular motion; energy; linear/angular momentum; systems of particles; rigid body motion; wave motion and sound.', 3, False, TRUE),
('PHYS', 225, 'L', 'Fundamental Physics: Laboratory', 'Laboratory for PHYS 225. Instructional fee required. (3 hours laboratory)', 1, False, TRUE),
('PHYS', 226, '', 'Fundamental Physics: Electricity and Magnetism', 'Electrostatics, electric potential, capacitance, dielectrics, electrical circuits, resistance, emf, electromagnetic induction, magnetism and magnetic materials, and introduction to Maxwell’s equations.', 3, False, TRUE),
('PHYS', 226, 'L', 'Fundamental Physics: Laboratory', 'Laboratory for PHYS 226. Instructional fee required. (3 hours laboratory)', 1, False, TRUE),
('PHYS', 227, '', 'Fundamental Physics: Waves, Optics, and Modern Physics', 'Geometrical and physical optics, wave phenomena; quantum physics, including the photoelectric effect, line spectra and the Bohr atom; the wave nature of matter, Schroedinger’s equation and solutions; the Uncertainty Principle, special theory of relativity.', 3, False, TRUE),
('PHYS', 227, 'L', 'Fundamental Physics: Laboratory', 'Laboratory for PHYS 227. Instructional fee required. (3 hours laboratory)', 1, False, TRUE),
('CPSC', 254, '', 'Software Development with Open Source Systems', 'Philosophy of open source software development, open source operating systems such as Linux; open source development tools; open source programming languages, such as Python; open source software development processes; open source software licensing issues. (2 hours lecture, 2 hours laboratory)', 3, False, TRUE),
('CPSC', 301, '', 'Programming Lab Practicum', 'Intensive programming covering concepts learned in lower-division courses. Procedural and object oriented design, documentation, arrays, classes, file input/output, recursion, pointers, dynamic variables, data and file structures.', 2, False, TRUE),
('CPSC', 349, '', 'Web Front-End Engineering', 'Concepts and architecture of interactive web applications, including markup, stylesheets and behavior. Functional and object-oriented aspects of JavaScript. Model-view design patterns, templates and frameworks. Client-side technologies for asynchronous events, real-time interaction and access to back-end web services.', 3, False, TRUE),
('CPSC', 375, '', 'Introduction to Data Science and Big Data', 'Techniques for data preparation, exploratory analysis, statistical modeling, machine learning and visualization. Methods for analyzing different types of data, such as natural language and time-series, from emerging applications, including Internet-of-Things. Big data platforms. Projects with real-world data.', 3, False, TRUE),
('CPSC', 386, '', 'Introduction to Game Design and Production', 'Current and future technologies and market trends in game design and production. Game technologies, basic building tools for games and the process of game design, development and production.', 3, False, TRUE),
('CPSC', 411, '', 'Mobile Device Application Programming', 'Introduction to developing applications for mobile devices, including but not limited to runtime environments, development tools and debugging tools used in creating applications for mobile devices. Use emulators in lab. Students must provide their own mobile devices.', 3, True, TRUE),
('CPSC', 431, '', 'Database and Applications', 'Database design and application development techniques for a real world system. System analysis, requirement specifications, conceptual modeling, logic design, physical design and web interface development. Develop projects using contemporary database management system and web-based application development platform.', 3, True, TRUE),
('CPSC', 439, '', 'Theory of Computation', 'Introduction to the theory of computation. Automata theory; finite state machines, context free grammars, and Turing machines; hierarchy of formal language classes. Computability theory and undecidable problems. Time complexity; P and NP-complete problems. Applications to software design and security.', 3, True, TRUE),
('CPSC', 440, '', 'Computer System Architecture', 'Computer performance, price/performance, instruction set design and examples. Processor design, pipelining, memory hierarchy design and input/output subsystems.', 3, True, TRUE),
('CPSC', 449, '', 'Web Back-End Engineering', 'Design and architecture of large-scale web applications. Techniques for scalability, session management and load balancing. Dependency injection, application tiers, message queues, web services and REST architecture. Caching and eventual consistency. Data models, partitioning and replication in relational and non-relational databases.', 3, True, TRUE),
('CPSC', 452, '', 'Cryptography', 'Introduction to cryptography and steganography. Encryption, cryptographic hashing, certificates, and signatures. Classical, symmetric-key, and public-key ciphers. Block modes of operation. Cryptanalysis including exhaustive search, man-in-the-middle, and birthday attacks. Programing projects involving implementation of cryptographic systems.', 3, True, TRUE),
('CPSC', 454, '', 'Cloud Computing and Security', 'Cloud computing and cloud security, distributed computing, computer clusters, grid computing, virtual machines and virtualization, cloud computing platforms and deployment models, cloud programming and software environments, vulnerabilities and risks of cloud computing, cloud infrastructure protection, data privacy and protection.', 3, True, TRUE),
('CPSC', 455, '', 'Web Security', 'Concepts of web application security. Web security mechanisms, including authentication, access control and protecting sensitive data. Common vulnerabilities, including code and SQL attacks, cross-site scripting and cross-site request forgery. Implement hands-on web application security mechanisms and security testing.', 3, True, TRUE),
('CPSC', 456, '', 'Network Security Fundamentals', 'Learn about vulnerabilities of network protocols, attacks targeting confidentiality, integrity and availability of data transmitted across networks, and methods for diagnosing and closing security gaps through hands-on exercises.', 3, True, TRUE),
('CPSC', 458, '', 'Malware Analysis', 'Introduction to principles and practices of malware analysis. Topics include static and dynamic code analysis, data decoding, analysis tools, debugging, shellcode analysis, reverse engineering of stealthy malware and written presentation of analysis results.', 3, True, TRUE),
('CPSC', 459, '', 'Blockchain Technologies', 'Digital assets as a medium of exchange to secure financial transactions; decentralized and distributed ledgers that record verifiable transactions; smart contracts and Ethereum; Bitcoin mechanics and mining; the cryptocurrency ecosystem; blockchain mechanics and applications.', 3, True, TRUE),
('CPSC', 462, '', 'Software Design', 'Concepts of software modeling, software process and some tools. Object-oriented analysis and design and Unified process. Some computer-aided software engineering (CASE) tools will be recommended to use for doing homework assignments.', 3, True, TRUE),
('CPSC', 463, '', 'Software Testing', 'Software testing techniques, reporting problems effectively and planning testing projects. Students apply what they learned throughout the course to a sample application that is either commercially available or under development.', 3, True, TRUE),
('CPSC', 464, '', 'Software Architecture', 'Basic principles and practices of software design and architecture. High-level design, software architecture, documenting software architecture, software and architecture evaluation, software product lines and some considerations beyond software architecture.', 3, True, TRUE),
('CPSC', 466, '', 'Software Process', 'Practical guidance for improving the software development process. How to establish, maintain and improve software processes. Exposure to agile processes, ISO 12207 and CMMI.', 3, False, TRUE),
('CPSC', 474, '', 'Parallel and Distributed Computing', 'Concepts of distributed computing; distributed memory and shared memory architectures; parallel programming techniques; inter-process communication and synchronization; programming for parallel architectures such as multi-core and GPU platforms; project involving distributed application development.', 3, True, TRUE),
('CPSC', 480, '', 'Introduction to High Performance Computing', 'Introduction to the concepts of high-performance computing and the paradigms of parallel programming in a high level programming language, design and implementation of parallel algorithms on distributed memory, machine learning techniques on large data sets, implementation of parallel algorithms.', 3, True, TRUE),
('CPSC', 483, '', 'Introduction to Machine Learning', 'Design, implement and analyze machine learning algorithms, including supervised learning and unsupervised learning algorithms. Methods to address uncertainty. Projects with real-world data.', 3, True, TRUE),
('CPSC', 484, '', 'Principles of Computer Graphics', 'Examine and analyze computer graphics, software structures, display processor organization, graphical input/output devices, display files. Algorithmic techniques for clipping, windowing, character generation and viewpoint transformation.', 3, True, TRUE),
('CPSC', 485, '', 'Computational Bioinformatics', 'Algorithmic approaches to biological problems. Specific topics include motif finding, genome rearrangement, DNA sequence comparison, sequence alignment, DNA sequencing, repeat finding and gene expression analysis.', 3, True, TRUE),
('CPSC', 486, '', 'Game Programming', 'Survey of data structures and algorithms used for real-time rendering and computer game programming. Build upon existing mathematics and programming knowledge to create interactive graphics programs.', 3, True, TRUE),
('CPSC', 489, '', 'Game Development Project', 'Individually or in teams, students design, plan and build a computer game.', 3, True, TRUE),
('CPSC', 499, '', 'Independent Study', 'Special topic in computer science, selected in consultation with and completed under the supervision of instructor. May be repeated for a maximum of 9 units of Undergraduate credit and 6 units of Graduate credit. Requires approval by the Computer Science chair.', 3, False, TRUE),
('EGGN', 495, '', 'Professional Practice', 'Professional engineering work in industry or government. Written report required. May be taken for credit for a maximum of three units. Applicable towards bachelor’s degree programs. Not for credit in the graduate program.', 3, False, TRUE),
('MATH', 335, '', 'Mathematical Probability', 'Probability theory; discrete, continuous and multivariate probability distributions, independence, conditional probability distribution, expectation, moment generating functions, functions of random variables and the central limit theorem.', 4, False, TRUE),
('MATH', 340, '', 'Numerical Analysis', 'Approximate numerical solutions of systems of linear and nonlinear equations, interpolation theory, numerical differentiation and integration, numerical solution of ordinary differential equations. Computer coding of numerical methods.', 4, False, TRUE),
('MATH', 370, '', 'Mathematical Model Building', 'Introduction to mathematical models in science and engineering. Dimensional analysis, discrete and continuous dynamical systems, and numerous other topics. Emphasizes deriving equations and using mathematical tools to make predictions.', 4, False, TRUE),
('HONR', 201, 'B', 'Honors Seminar: American Institutions and Values since 1877', 'Critically examines the development of American institutions and values from Reconstruction to present day, with particular reference to California government and politics. The interaction, conflict and cooperation of diverse groups with specific attention to race, ethnicity, gender and class.', 3, False, TRUE);



INSERT INTO COURSEPREREQ (COURSEDEPT, COURSENUM, COURSELETTER, PREREQDEPT, PREREQNUM, PREREQCOURSELETTER, ISCOREQ) VALUES
('CPSC', 120, '', 'MATH', 125, '', True),
('CPSC', 121, '', 'CPSC', 120, '', False),
('CPSC', 131, '', 'CPSC', 121, '', False),
('CPSC', 223, 'C', 'CPSC', 131, '', False),
('CPSC', 223, 'J', 'CPSC', 131, '', False),
('CPSC', 223, 'N', 'CPSC', 131, '', False),
('CPSC', 223, 'P', 'CPSC', 131, '', False),
('CPSC', 240, '', 'CPSC', 131, '', False),
('CPSC', 240, '', 'MATH', 170, 'A', False),
('CPSC', 240, '', 'MATH', 280, '', False),
('CPSC', 315, '', 'CPSC', 131, '', False),
('CPSC', 323, '', 'CPSC', 131, '', False),
('CPSC', 332, '', 'CPSC', 131, '', False),
('CPSC', 335, '', 'MATH', 170, 'B', False),
('CPSC', 335, '', 'CPSC', 131, '', False),
('CPSC', 351, '', 'CPSC', 131, '', False),
('CPSC', 362, '', 'CPSC', 131, '', False),
('CPSC', 471, '', 'CPSC', 351, '', False),
('CPSC', 481, '', 'CPSC', 335, '', False),
('CPSC', 481, '', 'MATH', 338, '', False),
('CPSC', 490, '', 'CPSC', 362, '', False),
('CPSC', 491, '', 'CPSC', 490, '', False),
('MATH', 150, 'A', 'MATH', 125, '', False),
('MATH', 150, 'B', 'MATH', 150, 'A', False),
('MATH', 338, '', 'MATH', 130, '', False),
('MATH', 338, '', 'MATH', 150, 'B', False),
('BIOL', 101, 'L', 'BIOL', 101, '', True),
('BIOL', 101, 'L', 'BIOL', 103, '', True),
('BIOL', 152, '', 'BIOL', 151, '', False),
('CHEM', 120, 'A', 'CHEM', 115, '', False),
('CHEM', 120, 'B', 'CHEM', 120, 'A', False),
('CHEM', 123, '', 'MATH', 125, '', True),
('CHEM', 123, '', 'MATH', 150, 'A', True),
('CHEM', 125, '', 'CHEM', 120, 'A', False),
('CHEM', 125, '', 'CHEM', 123, '', False),
('GEOL', 101, 'L', 'GEOL', 101, '', True),
('GEOL', 101, 'L', 'GEOL', 110, 'T', True),
('GEOL', 201, '', 'GEOL', 101, 'L', False),
('GEOL', 201, '', 'GEOL', 102, '', False),
('GEOL', 201, 'L', 'GEOL', 201, '', True),
('MATH', 250, 'A', 'MATH', 150, 'B', False),
('MATH', 250, 'B', 'MATH', 250, 'A', False),
('PHYS', 225, '', 'MATH', 150, 'A', False),
('PHYS', 225, 'L', 'PHYS', 225, '', True),
('PHYS', 226, '', 'MATH', 150, 'B', False),
('PHYS', 226, '', 'PHYS', 225, '', False),
('PHYS', 226, 'L', 'PHYS', 226, '', True),
('PHYS', 227, '', 'PHYS', 226, '', False),
('PHYS', 227, 'L', 'PHYS', 227, '', True),
('CPSC', 254, '', 'CPSC', 131, '', False),
('CPSC', 301, '', 'CPSC', 131, '', False),
('CPSC', 349, '', 'CPSC', 131, '', False),
('CPSC', 375, '', 'CPSC', 131, '', False),
('CPSC', 375, '', 'MATH', 338, '', False),
('CPSC', 386, '', 'CPSC', 121, '', False),
('CPSC', 411, '', 'CPSC', 131, '', False),
('CPSC', 431, '', 'CPSC', 332, '', False),
('CPSC', 439, '', 'CPSC', 121, '', False),
('CPSC', 439, '', 'MATH', 320, '', False),
('CPSC', 439, '', 'MATH', 170, 'B', False),
('CPSC', 439, '', 'MATH', 280, '', False),
('CPSC', 440, '', 'CPSC', 240, '', False),
('CPSC', 449, '', 'CPSC', 332, '', False),
('CPSC', 452, '', 'MATH', 170, 'B', False),
('CPSC', 452, '', 'CPSC', 131, '', False),
('CPSC', 454, '', 'CPSC', 351, '', False),
('CPSC', 454, '', 'CPSC', 253, '', False),
('CPSC', 455, '', 'CPSC', 351, '', False),
('CPSC', 455, '', 'CPSC', 353, '', False),
('CPSC', 456, '', 'CPSC', 351, '', False),
('CPSC', 458, '', 'CPSC', 351, '', False),
('CPSC', 459, '', 'CPSC', 351, '', False),
('CPSC', 459, '', 'CPSC', 253, '', False),
('CPSC', 459, '', 'CPSC', 452, '', False),
('CPSC', 462, '', 'CPSC', 362, '', False),
('CPSC', 463, '', 'CPSC', 362, '', False),
('CPSC', 464, '', 'CPSC', 362, '', False),
('CPSC', 466, '', 'CPSC', 362, '', False),
('CPSC', 474, '', 'CPSC', 351, '', False),
('CPSC', 480, '', 'CPSC', 351, '', False),
('CPSC', 483, '', 'CPSC', 335, '', False),
('CPSC', 483, '', 'MATH', 338, '', False),
('CPSC', 484, '', 'CPSC', 131, '', False),
('CPSC', 484, '', 'MATH', 150, 'B', False),
('CPSC', 484, '', 'MATH', 170, 'B', False),
('CPSC', 485, '', 'CPSC', 131, '', False),
('CPSC', 486, '', 'CPSC', 386, '', False),
('CPSC', 486, '', 'CPSC', 484, '', False),
('CPSC', 489, '', 'CPSC', 486, '', False),
('MATH', 335, '', 'MATH', 250, 'A', False),
('MATH', 340, '', 'MATH', 250, 'B', False),
('MATH', 340, '', 'MATH', 320, '', False),
('MATH', 340, '', 'CPSC', 120, '', False),
('MATH', 340, '', 'CPSC', 121, '', False),
('MATH', 370, '', 'MATH', 250, 'B', False),
('MATH', 370, '', 'MATH', 320, '', False),
('MATH', 370, '', 'CPSC', 120, '', False),
('MATH', 370, '', 'CPSC', 121, '', False);


#QUERIES

#LIST ALL COURSES AND THEIR PREREQUISITES
SELECT * FROM COURSE AS C LEFT JOIN COURSEPREREQ AS P ON 
C.DEPTCODE = P.COURSEDEPT AND C.COURSENUM=P.COURSENUM AND C.COURSELETTER = P.COURSELETTER;

#LIST ALL COURSES THAT ARE A PREREQISITE OF CLASS SPECIFIED
SELECT * FROM COURSE AS C, COURSEPREREQ AS P
WHERE P.COURSEDEPT = 'CPSC' AND P.COURSENUM = 131 AND P.COURSELETTER = '' AND 
C.DEPTCODE = P.PREREQDEPT AND C.COURSENUM = P.PREREQNUM AND C.COURSELETTER = P.PREREQCOURSELETTER;

#LIST ALL COURSES THAT HAVE SPECIFIED CLASS AS A PREREQUISITE (AKA POSTREQS)
SELECT * FROM COURSEPREREQ AS P
WHERE P.PREREQDEPT = 'CPSC' AND P.PREREQNUM = 131 AND P.PREREQCOURSELETTER = '';

#LIST ALL COURSES 2 CLASSES ABOVE SPECIFIED

SELECT * FROM COURSEPREREQ AS CP JOIN
(SELECT COURSEDEPT AS CD, COURSENUM AS CN , PREREQCOURSELETTER AS PN FROM COURSEPREREQ AS P
WHERE P.PREREQDEPT = 'CPSC' AND P.PREREQNUM = 131 AND P.PREREQCOURSELETTER = '') AS FP ON CP.PREREQDEPT = CD AND CP.PREREQNUM = CN AND CP.PREREQCOURSELETTER = PN;

#LIST ALL UNDERGRAD CLASSES AVAILABLE FOR GRAD CREDIT
SELECT * FROM COURSE
WHERE GRADCREDIT = TRUE;

