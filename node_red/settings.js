module.exports = {
    // Auto-generate a secure credential secret (32-byte hex)
    credentialSecret: require("crypto").randomBytes(32).toString('hex'),
    
    // Enable HTTPS with self-signed certs (for WSS)
    https: {
        key: require("fs").readFileSync(require("path").join(__dirname, 'certs/server-key.pem')),
        cert: require("fs").readFileSync(require("path").join(__dirname, 'certs/server-cert.pem')),
        ca: require("fs").readFileSync(require("path").join(__dirname, 'certs/ca.pem'))
    },

    // Secure admin authentication
    adminAuth: {
        type: "credentials",
        users: [{
            username: "iotadmin",
            password: "$2a$08$5B8zHyrPl5Jsj1yZ0QY7A.LD.8X1Zb5JhT7cR9v2KkM3wY1NqRtO6" // 'SecurePass123!' encrypted
        }]
    },

    // Secure Node-RED editor and HTTP nodes
    editorTheme: {
        page: {
            title: "Industrial IoT Dashboard",
            favicon: "/absolute/path/to/your/favicon.ico"
        },
        login: {
            image: "/absolute/path/to/login-background.jpg"
        }
    },

    // Security middleware
    security: {
        enable: true,
        allowWeakPasswords: false,
        secret: require("crypto").randomBytes(32).toString('hex')
    },

    // CORS restrictions
    httpNodeCors: {
        origin: "https://your-domain.com",
        methods: "GET,PUT,POST,DELETE"
    },

    // File locations
    userDir: require("path").join(__dirname, ".node-red"),
    nodesDir: require("path").join(__dirname, "nodes"),

    // Logging
    logging: {
        console: {
            level: "info",
            metrics: false,
            audit: true
        }
    },

    // Runtime settings
    runtimeState: {
        enabled: true,
        ui: true
    }
};