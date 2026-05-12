import streamlit as st 

st.write(":world_map: hello world folks " )

st.header("this is Header" , divider = True)
st.subheader("this is sub header",)
st.text("hello")
st.markdown(":red[**hello**] *world* :world_map:")
st.markdown(":red-background[:orange[**hello**]]")

#name input 
name = st.text_input("Enter your name")
st.write(name)

#number input 
age = st.number_input("Enter your age" , value = None)
st.write(age)
#print(type(age))

pressed = st.button(":red-background Confirm")

if pressed :
    st.write("confirmed")

selected = st.selectbox("Choose one" ,
                         ("student" , "Employer") ,
                         index=None ,
                         accept_new_options = True)

st.write("You seleted " , selected)





#..\\.venv\\Scripts\\Activate.ps1  -- to activate the virtual environment in powershell  
#python -m streamlit run text-input.py  -- for run (recomended)