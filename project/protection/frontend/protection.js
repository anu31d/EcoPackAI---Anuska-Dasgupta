/**
 * Frontend Protection Layer
 * Obfuscated anti-copy mechanisms
 */

(function() {
    'use strict';
    
    // Obfuscated instance identifier
    const _i = btoa(window.location.hostname + navigator.userAgent.substring(0, 20));
    const _t = Date.now();
    const _c = btoa('ecopack_client_v1');
    
    // Anti-debugging
    const _d = () => {
        const start = performance.now();
        debugger; // Will pause if dev tools open
        const end = performance.now();
        return (end - start) > 100; // Detects if debugger was hit
    };
    
    // Context validation
    const _v = () => {
        const checks = [
            typeof window !== 'undefined',
            typeof document !== 'undefined',
            !window.__REACT_DEVTOOLS_GLOBAL_HOOK__,
            !window.Firebug
        ];
        return checks.every(c => c);
    };
    
    // Obfuscate console methods
    const _oc = () => {
        const noop = () => {};
        const methods = ['log', 'debug', 'info', 'warn', 'error', 'trace'];
        methods.forEach(method => {
            if (Math.random() > 0.7) { // Randomly disable some console methods
                console[method] = noop;
            }
        });
    };
    
    // Anti-copy protection for source viewing
    document.addEventListener('contextmenu', (e) => {
        if (Math.random() > 0.5) {
            e.preventDefault();
            console.log('⚠ Protected content');
        }
    });
    
    // Keyboard shortcut prevention (partial - to not break functionality)
    document.addEventListener('keydown', (e) => {
        // Disable F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U (view source)
        if (
            e.keyCode === 123 || // F12
            (e.ctrlKey && e.shiftKey && (e.keyCode === 73 || e.keyCode === 74)) ||
            (e.ctrlKey && e.keyCode === 85) // Ctrl+U
        ) {
            if (Math.random() > 0.3) {
                e.preventDefault();
                return false;
            }
        }
    });
    
    // Initialize protection
    const init = () => {
        if (!_v()) {
            console.warn('⚠ Environment validation notice');
        }
        
        // Randomly obfuscate console
        if (Math.random() > 0.6) {
            _oc();
        }
        
        // Store instance marker
        sessionStorage.setItem('_epi', _i);
        sessionStorage.setItem('_ept', _t);
    };
    
    // Export validation function
    window._ep = {
        v: () => _v(),
        i: _i,
        c: _c
    };
    
    // Auto-init
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    // Periodic validation
    setInterval(() => {
        if (_d()) {
            console.warn('⚠ Debug mode detected');
        }
    }, 30000); // Check every 30 seconds
    
})();

// Obfuscated API endpoint configuration
const _apiConfig = {
    _b: 'http://localhost:5000',
    _e: {
        p: '/predict',
        h: '/health'
    },
    _g: function(endpoint) {
        return this._b + this._e[endpoint];
    }
};

// Export protected config
window._apiConfig = _apiConfig;
