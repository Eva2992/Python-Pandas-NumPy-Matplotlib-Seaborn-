import streamlit as st 

st.title("Information " , anchor= False)
st.divider()

images = st.file_uploader("Enter your file" ,
                 type =['jpg' , 'jpeg' , 'png'] ,
                 accept_multiple_files= True)

st.image("media/photo.png")
st.video("media/video.mkv")

#image input 

if images :
    col =  st.columns(len(images))

    for i , image in enumerate(images) :
      with col[i] : st.image(image)


#video upload 

video_file = st.file_uploader("Enter your video" ,
                           type =['mkv' , 'mp4']) 

button = st.button("click to upload")

if button :
   if video_file :
      st.video(video_file)
      st.success("Successfully uploaded")
   else :
      st.error("Upload the video")   
