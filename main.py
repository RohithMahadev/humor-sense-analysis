import streamlit as st 
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image
from datetime import datetime


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)


image = Image.open('pic_1.png')

st.image(image, caption='Humor sense',use_column_width = "auto")
df = pd.read_csv('data.csv')




html_temp = """
		
		<h1 style="color:{};text-align:center;">what is your humour sense?</h1>
		</div>
		"""

st.markdown(html_temp.format('#55386C'),unsafe_allow_html=True)

about = """
		
		<h3 style="color:{};">Humor sense is a personality that gives someone the ability to say funny things and see the funny side of things</h1>
		<br><br></div>
		"""

st.markdown(about.format('black'),unsafe_allow_html=True)


def questions(i):
	mapped_val = {
		 1:'Never or very rarely true',
			2:'Rarely true',
			3: 'Sometimes true',
			4: 'Often true',
			5:'Very often or always true '
				}
	val = st.selectbox('select a range',(i for i in mapped_val.values()),key = i)
	for key,vals in mapped_val.items():
		if vals == val:
			return key

#q1 
ques_1= st.markdown("<h5 style='color: #D16161;'><b>1. I usually don't laugh or joke around much with other people.</b></h5>", unsafe_allow_html=True)
ques_1_scale = questions(1)
#q2

ques_2 = st.markdown("<h5 style='color:#D16161;'><b>2. If I am feeling depressed, I can usually cheer myself up with humor.</b></h5>", unsafe_allow_html=True)
ques_2_scale = questions(2)

#q3
ques_3 = st.markdown("<h5 style='color: #D16161;'><b>3. If someone makes a mistake, I will often tease them about it..</b></h5>", unsafe_allow_html=True)
ques_3_scale = questions(3)


#q4
ques_4 = st.markdown("<h5 style='color: #D16161;'><b>4. I let people laugh at me or make fun at my expense more than I should.</b></h5>", unsafe_allow_html=True)
ques_4_scale = questions(4)


#q5
ques_5 = st.markdown("<h5 style='color: #D16161;'><b>5. I don't have to work very hard at making other people laugh. I seem to be a naturally humorous person.</b></h5>", unsafe_allow_html=True)
ques_5_scale = questions(5)

#q6
ques_6 = st.markdown("<h5 style='color: #D16161;'><b>6. Even when I am by myself, I am often amused by the absurdities of life.</b></h5>", unsafe_allow_html=True)
ques_6_scale = questions(6)

#q7
ques_7 = st.markdown("<h5 style='color: #D16161;'><b>7. People are never offended or hurt by my sense of humor.</b></h5>", unsafe_allow_html=True)
ques_7_scale = questions(7)

#q8
ques_8 = st.markdown("<h5 style='color: #D16161;'><b>8. I will often get carried away in putting myself down if it makes my family or friends laugh.</b></h5>", unsafe_allow_html=True)
ques_8_scale = questions(8)

#q9
ques_9 = st.markdown("<h5 style='color: #D16161;'><b>9. I rarely make other people laugh by telling funny stories about myself.</b></h5>", unsafe_allow_html=True)
ques_9_scale = questions(9)

#q10
ques_10 = st.markdown("<h5 style='color: #D16161;'><b>10. If I am feeling upset or unhappy I usually try to think of something funny about the situation to make myself feel better.</b></h5>", unsafe_allow_html=True)
ques_10_scale = questions(10)


#q11
ques_11 = st.markdown("<h5 style='color: #D16161;'><b>11. When telling jokes or saying funny things, I am usually not very concerned about how other people are taking it.</b></h5>", unsafe_allow_html=True)
ques_11_scale = questions(11)

#q12
ques_12 = st.markdown("<h5 style='color: #D16161;'><b>12. I often try to make people like or accept me more by saying something funny about my own weaknesses, blunders, or faults.</b></h5>", unsafe_allow_html=True)
ques_12_scale = questions(12)

#q13
ques_13 = st.markdown("<h5 style='color: #D16161;'><b>13. I laugh and joke a lot with my closest friends.</b></h5>", unsafe_allow_html=True)
ques_13_scale = questions(13)

#q14
ques_14 = st.markdown("<h5 style='color: #D16161;'><b>14. My humorous outlook on life keeps me from getting overly upset or depressed about things.</b></h5>", unsafe_allow_html=True)
ques_14_scale = questions(14)

#q15
ques_15 = st.markdown("<h5 style='color: #D16161;'><b>15. I do not like it when people use humor as a way of criticizing or putting someone down.</b></h5>", unsafe_allow_html=True)
ques_15_scale = questions(15)

#q16
ques_16 = st.markdown("<h5 style='color: #D16161;'><b>16. I do not often say funny things to put myself down.</b></h5>", unsafe_allow_html=True)
ques_16_scale = questions(16)

st.markdown("<h3 style='color: PURPLE;'><br><br><b>YOU HAVE MADE IT HAVE WAY THROUGH !</b><br><br></h5>", unsafe_allow_html=True)


#q17
ques_17 = st.markdown("<h5 style='color: black;'><b>17. I usually do not like to tell jokes or amuse people.</b></h5>", unsafe_allow_html=True)
ques_17_scale = questions(17)

#q18
ques_18 = st.markdown("<h5 style='color: black;'><b>18. If I am by myself and I am feeling unhappy, I make an effort to think of something funny to cheer myself up..</b></h5>", unsafe_allow_html=True)
ques_18_scale = questions(18)

#q19
ques_19 = st.markdown("<h5 style='color: black;'><b>19. Sometimes I think of something that is so funny that I can not stop myself from saying it, even if it is not appropriate for the situation.</b></h5>", unsafe_allow_html=True)
ques_19_scale = questions(19)


#q20
ques_20 = st.markdown("<h5 style='color: black;'><b>20. I often go overboard in putting myself down when I am making jokes or trying to be funny.</b></h5>", unsafe_allow_html=True)
ques_20_scale = questions(20)

#q21
ques_21 = st.markdown("<h5 style='color: black;'><b>21. I enjoy making people laugh.</b></h5>", unsafe_allow_html=True)
ques_21_scale = questions(21)

#q22
ques_22 = st.markdown("<h5 style='color: black;'><b>22. If I am feeling sad or upset, I usually lose my sense of humor.</b></h5>", unsafe_allow_html=True)
ques_22_scale = questions(22)

#q23
ques_23 = st.markdown("<h5 style='color: black;'><b>23. I never participate in laughing at others even if all my friends are doing it.</b></h5>", unsafe_allow_html=True)
ques_23_scale = questions(23)

#q24
ques_24 = st.markdown("<h5 style='color: black;'><b>24. When I am with friends or family, I often seem to be the one that other people make fun of or joke about.</b></h5>", unsafe_allow_html=True)
ques_24_scale = questions(24)

#q25
ques_25 = st.markdown("<h5 style='color: black;'><b>25. I do not often joke around with my friends.</b></h5>", unsafe_allow_html=True)
ques_25_scale = questions(25)

#q26
ques_26 = st.markdown("<h5 style='color: black;'><b>26. It is my experience that thinking about some amusing aspect of a situation is often a very effective way of coping with problems.</b></h5>", unsafe_allow_html=True)
ques_26_scale = questions(26)

#q27
ques_27 = st.markdown("<h5 style='color: black;'><b>27. If I do not like someone, I often use humor or teasing to put them down.</b></h5>", unsafe_allow_html=True)
ques_27_scale = questions(27)

#q28
ques_28 = st.markdown("<h5 style='color: black;'><b>28. If I am having problems or feeling unhappy, I often cover it up by joking around, so that even my closest friends do not know how I really feel.</b></h5>", unsafe_allow_html=True)
ques_28_scale = questions(28)

#q29
ques_29 = st.markdown("<h5 style='color: black;'><b>29. I usually cannot think of witty things to say when I am with other people.</b></h5>", unsafe_allow_html=True)
ques_29_scale = questions(29)

#q30
ques_30 = st.markdown("<h5 style='color: black;'><b>30. I donot need to be with other people to feel amused. I can usually find things to laugh about even when I am by myself.</b></h5>", unsafe_allow_html=True)
ques_30_scale = questions(30)

#q31
ques_31 = st.markdown("<h5 style='color: black;'><b> 31. Even if something is really funny to me, I will not laugh or joke about it if someone will be offended..</b></h5>", unsafe_allow_html=True)
ques_31_scale = questions(31)

#q32
ques_32 = st.markdown("<h5 style='color: black;'><b> 32. Letting others laugh at me is my way of keeping my friends and family in good spirits.</b></h5>", unsafe_allow_html=True)
ques_32_scale = questions(32)

btn_val = st.button("Find answers")


if btn_val is True:

	affiliative =  np.round( ( (6-ques_1_scale) + ques_5_scale + (6-ques_9_scale) + ques_13_scale + (6-ques_17_scale) + ques_21_scale + (6-ques_25_scale) + (6-ques_29_scale))/8, 1)
	selfenhancing = np.round((ques_2_scale + ques_6_scale + ques_10_scale + ques_14_scale + ques_18_scale + ques_22_scale + ques_26_scale + ques_30_scale)/8,1)
	aggressive =  np.round((ques_3_scale+ ques_7_scale + ques_11_scale+ ques_15_scale + ques_19_scale + ques_23_scale + ques_27_scale + ques_31_scale)/8,1)
	selfdefeating = np.round((ques_4_scale + ques_8_scale + ques_12_scale+ ques_16_scale + ques_20_scale + ques_24_scale + ques_28_scale + ques_32_scale)/8,1)
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	answers = pd.DataFrame([dt_string,affiliative,selfenhancing,aggressive,selfdefeating])
	answers = answers.T

	

	fig_1 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = affiliative,
    title = {'text': "affiliative"},
	 domain = {'x': [0, 1], 'y': [0, 1]},
	gauge = {'axis': {'range': [0, 5]}},
    
		))

	fig_2 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = selfenhancing,
    title = {'text': "selfenhancing"},
	gauge = {'axis': {'range': [0, 5]}},
	 domain = {'x': [0, 1], 'y': [0, 1]}
    
		))

	fig_3 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = aggressive,
    title = {'text': "aggressive"},
	gauge = {'axis': {'range': [0, 5]}},
	 domain = {'x': [0, 1], 'y': [0, 1]}
  
		))

	fig_4 = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = selfdefeating,
    title = {'text': "selfdefeating"},
	gauge = {'axis': {'range': [0, 5]}},
	 domain = {'x': [0, 1], 'y': [0, 1]}
   
		))

	st.markdown("<h5 style='color: PURPLE;'><br><h3>Affliative humor</h3><br><b>This involves telling jokes about things that everyone might find funny. The goal is to use humor to bring people together to find the humor in everyday life. The types of jokes told by comedians like Jerry Seinfeld that focus on the comedy in everyday life represents this sort of humor. The goal is to create a sense of fellowship, happiness, and well-being. If you are fond of jokes about animals or everyday occurrences, then you are using affiliative humor.</b><br><br></h5>", unsafe_allow_html=True)


	st.plotly_chart(fig_1,use_container_width=True)
	st.markdown("<h5 style='color: PURPLE;'><br><h3>Aggressive humor</h3><br><b>This involves put-downs or insults targeted toward individuals. This is the humor that is used by more aggressive comedians—the put-down artists, such as Don Rickles or the late Joan Rivers. When it is intended to threaten or psychologically harm others, it is the type of humor used by bullies. While some of the audience to this type of humor will find it funny, others might laugh to cover up a feeling of discomfort.</b><br><br></h5>", unsafe_allow_html=True)

	st.plotly_chart(fig_2,use_container_width=True)
	st.markdown("<h5 style='color: PURPLE;'><br><h3>Self-enhancing humor.</h3><br><b> This is being able to laugh at yourself, such as making a joke when something bad has happened to you. Trying to find the humor in everyday situations, and making yourself the target of the humor in a good-natured way. It is related to healthy coping with stress. Jon Stewart from the Daily Show often uses self-enhancing humor by saying things such as, Maybe I just dont understand, or I am not the brightest guy.<br></h5>", unsafe_allow_html=True)

	st.plotly_chart(fig_3,use_container_width=True)
	
	st.markdown("<h5 style='color: PURPLE;'><br><h3> Self-defeating humor</h3><br><b>Putting yourself down in an aggressive or “poor me” fashion is called self-defeating humor. The late comedian Rodney Dangerfield would be an example (“I don’t get no respect” “I was an ugly baby”). Psychologically, this can be an unhealthy form of humor, and is sometimes used by targets of bullies to try to avoid attacks—making oneself the butt of jokes before others put you down.</b><br><br></h5>", unsafe_allow_html=True)

	st.plotly_chart(fig_4,use_container_width=True)

	
	path = 'test_data.csv'
	with open(path, 'a') as file:
		answers.to_csv(file,index = False, header = False)

	st.balloons()


