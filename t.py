from app.summarizer import summarize

text = """
Artificial intelligence (AI) has emerged as one of the most transformative technologies of the 21st century. 
It is now deeply integrated into industries ranging from healthcare to finance, enabling automation, predictive analytics, and improved decision-making. 
Machine learning, a subset of AI, allows systems to learn patterns from data and make predictions with minimal human intervention. 
Deep learning, a specialized branch of machine learning, uses neural networks to process complex datasets such as images, speech, and natural language.

Despite its many benefits, AI also poses significant ethical challenges. 
Concerns include privacy invasion, job displacement due to automation, and biases in AI algorithms that can perpetuate social inequalities. 
To address these issues, researchers and policymakers are developing frameworks for responsible AI, emphasizing transparency, accountability, and fairness.

In addition, AI-powered tools are revolutionizing education and research. 
Intelligent tutoring systems can personalize learning for students, while AI-driven data analysis accelerates scientific discovery. 
However, the rapid pace of AI development means that continuous monitoring and regulation are essential to ensure societal benefits outweigh risks.

Looking ahead, AI is expected to continue reshaping economies, transforming human-computer interactions, and enabling innovations that were previously thought impossible. 
Collaboration between humans and AI systems will likely define the next era of technological progress, combining human creativity with computational power.

"""

print("\nSTUDENT SUMMARY:")
print(summarize(text, audience="student"))

print("\nPROFESSIONAL SUMMARY:")
print(summarize(text, audience="professional"))

print("\nRESEARCHER SUMMARY:")
print(summarize(text, audience="researcher"))
