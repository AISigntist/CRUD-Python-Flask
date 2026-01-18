# Sample blog data - array of 10 blogs
def get_blogs() -> list[dict]:
    return [
        {
            'id': 1,
            'title': 'Getting Started with Python Flask',
            'author': 'John Doe',
            'date': '2024-01-15',
            'excerpt': 'Learn the basics of Flask and how to build your first web application with this powerful Python framework. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Python'
        },
        {
            'id': 2,
            'title': 'Understanding RESTful APIs',
            'author': 'Jane Smith',
            'date': '2024-01-20',
            'excerpt': 'A comprehensive guide to designing and implementing RESTful APIs that follow best practices and conventions. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Web Development'
        },
        {
            'id': 3,
            'title': 'Database Design Best Practices',
            'author': 'Mike Johnson',
            'date': '2024-01-25',
            'excerpt': 'Explore essential principles for designing efficient and scalable database schemas for your applications. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Database'
        },
        {
            'id': 4,
            'title': 'Modern JavaScript ES6+ Features',
            'author': 'Sarah Williams',
            'date': '2024-02-01',
            'excerpt': 'Discover the powerful features introduced in ES6 and later versions that make JavaScript development more enjoyable. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'JavaScript'
        },
        {
            'id': 5,
            'title': 'Docker Containerization Guide',
            'author': 'David Brown',
            'date': '2024-02-05',
            'excerpt': 'Learn how to containerize your applications with Docker and deploy them efficiently across different environments. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'DevOps'
        },
        {
            'id': 6,
            'title': 'Building Responsive Web Designs',
            'author': 'Emily Davis',
            'date': '2024-02-10',
            'excerpt': 'Master the art of creating websites that look great on all devices using modern CSS techniques and frameworks. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Web Design'
        },
        {
            'id': 7,
            'title': 'Introduction to Machine Learning',
            'author': 'Robert Taylor',
            'date': '2024-02-15',
            'excerpt': 'Start your journey into machine learning with this beginner-friendly introduction to key concepts and algorithms. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Machine Learning'
        },
        {
            'id': 8,
            'title': 'Git Workflow Strategies',
            'author': 'Lisa Anderson',
            'date': '2024-02-20',
            'excerpt': 'Explore different Git workflow strategies that can help your team collaborate more effectively on software projects. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Version Control'
        },
        {
            'id': 9,
            'title': 'Cloud Computing Fundamentals',
            'author': 'Chris Martinez',
            'date': '2024-02-25',
            'excerpt': 'Understand the core concepts of cloud computing and how to leverage cloud services for your applications. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Cloud'
        },
        {
            'id': 10,
            'title': 'Security Best Practices for Web Apps',
            'author': 'Jennifer Lee',
            'date': '2024-03-01',
            'excerpt': 'Learn essential security practices to protect your web applications from common vulnerabilities and attacks. This is a test excerpt for the blog post.',
            'category': 'Security'
        },
        {
            'id': 11,
            'title': 'React Hooks and Functional Components',
            'author': 'Michael Brown',
            'date': '2024-03-05',
            'excerpt': 'Learn how to use React Hooks and functional components to build modern web applications. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'React'
        },
        {
            'id': 12,
            'title': 'Django REST Framework Tutorial',
            'author': 'Emily Davis',
            'date': '2024-03-10',
            'excerpt': 'Learn how to use Django REST Framework to build RESTful APIs for your web applications. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Django'
        },
        {
            'id': 13,
            'title': 'Python Decorators Explained',
            'author': 'Robert Taylor',
            'date': '2024-03-15',
            'excerpt': 'Learn how to use Python decorators to add functionality to your functions and classes. This is a test excerpt for the blog post. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.',
            'category': 'Python'
        }
    
    ]