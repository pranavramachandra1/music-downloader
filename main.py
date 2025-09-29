import streamlit as st
from music_download_mp3_return import download_audio_with_mp3

def stop_download():
    st.session_state.stop = True

def main():
    st.title('YouTube Audio Downloader')

    if 'stop' not in st.session_state:
        st.session_state.stop = False

    youtube_link = st.text_input('Enter YouTube link:')

    with st.form(key='download_form'):
        submit_button = st.form_submit_button(label='Download')

    stop_button = st.button("Stop")

    if stop_button:
        stop_download()

    if submit_button:
        if youtube_link:
            with st.spinner("Loading..."):
                st.write("Downloading audio...")
                if not st.session_state.stop:
                    data = download_audio_with_mp3(youtube_link)
                    
                    # Check if download was successful
                    if 'error' in data:
                        st.error(f"Download failed: {data['error']}")
                    else:
                        st.success("Download complete!")
                        
                        # Display the title
                        st.subheader(f"🎵 {data['title']}")
                        
                        # Create download button with the MP3 data
                        st.download_button(
                            label="📥 Download File",
                            data=data['data'],
                            file_name=data['filename'],
                            mime="audio/mpeg",
                            help="Click to download file"
                        )
                        
                        # Optional: Show file info
                        file_size_mb = len(data['data']) / (1024 * 1024)
                        st.info(f"File size: {file_size_mb:.2f} MB")
                        
                else:
                    st.warning("Download stopped!")
        else:
            st.error("Please enter a valid YouTube link")

if __name__ == "__main__":
    main()