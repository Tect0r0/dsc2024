import { useEffect } from 'react';

export default function Chatbot() {
    useEffect(() => {
        const script = document.createElement('script');
        script.src = 'https://cdn.botpress.cloud/webchat/v1/inject.js';
        script.async = true;
        script.onload = () => {
            const botpressConfig = document.createElement('script');
            botpressConfig.src = 'https://mediafiles.botpress.cloud/b82f249e-ad85-41ca-8f14-16a4f36b8507/webchat/config.js';
            botpressConfig.defer = true;
            document.body.appendChild(botpressConfig);
        };
        document.body.appendChild(script);

        return () => {
            // Clean up script elements when component unmounts
            document.body.removeChild(script);
            const existingConfig = document.querySelector('script[src^="https://mediafiles.botpress.cloud"]');
            if (existingConfig) {
                document.body.removeChild(existingConfig);
            }
        };
    }, []);

    return (
        <div className="page">
            <div className="page1">
                {/* This is where the Botpress chat widget will be injected */}
                <div id="bp-webchat"></div>
            </div>
          
        </div>
    );
}
