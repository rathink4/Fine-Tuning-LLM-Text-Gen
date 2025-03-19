mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"rathink4@email_id.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml