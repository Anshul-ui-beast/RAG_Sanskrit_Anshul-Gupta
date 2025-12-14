import os

# Create a directory for documents
if not os.path.exists("documents"):
    os.makedirs("documents")

# The Sanskrit content provided in the context 
sanskrit_text = """
[Story 1: The Foolish Servant]
अरे शंखनाद, गच्छापणम्, शर्कराम् आनय । इति स्वभृत्यम् शंखनादम् गोवर्धनदासः आदिशति ।
ततः शंखनादः आपणम् गच्छति, शर्कराम् जीर्णे वस्त्रे न्यस्यति च... [cite: 2-3]

[Story 2: Clever Kalidasa]
घोषितं कदाचित् भोजराज्ञा, यदि कोऽपि कविः मम दरबारे नूतनं काव्यं पठति तर्हि ददामि तस्मै लक्षरुप्यकाणि इति ।
परन्तु दरबारे अविद्यन्त केचन विद्वानाः ये कं अपि काव्यं प्रथमश्रुत्यनन्तरं एव सम्पूर्णतया पुनरोक्तुं शक्ताः... [cite: 14, 16]

[Story 3: The Old Woman's Cleverness]
आसीत् चित्रपुरम् नाम किमपि नगरं श्रीपर्वतस्य समीपे... घण्टाकर्णः नाम राक्षसः प्रतिवसती ति जनप्रवादः... 

[Story 4: The Devotee]
एकः परमः देवभक्तः अस्ति । सः प्रतिदिने भक्त्या देवस्य प्रार्थनाम् करोति... [cite: 38]

[Story 5: The Cold Hurts]
शीतं बहु बाधति । सर्वे जानन्ति यत् भोजराज्ञः दरबारे अविद्यत कविः कालीदासः... [cite: 57-58]
"""

# Save to a text file
with open("documents/sanskrit_stories.txt", "w", encoding="utf-8") as f:
    f.write(sanskrit_text)

print("✅ Sanskrit documents created successfully.")