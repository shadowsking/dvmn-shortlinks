if [ ! -d "venv" ]; then
    source install.sh
fi

source venv/scripts/activate
python ./python/dvmn_shortlinks/main.py
read -p "Press 'Enter' key to finish..."
