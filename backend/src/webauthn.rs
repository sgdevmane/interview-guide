//! Passkeys / WebAuthn Service (Item #39)
//! Provides passwordless FIDO2 / WebAuthn registration and authentication.
//! Supports TouchID, FaceID, Windows Hello, and Hardware Security Keys (YubiKey).

use std::sync::Arc;
use uuid::Uuid;
use webauthn_rs::prelude::*;

#[derive(Clone)]
pub struct WebAuthnService {
    webauthn: Arc<Webauthn>,
}

impl WebAuthnService {
    pub fn new(rp_id: &str, rp_origin_str: &str) -> Result<Self, String> {
        let rp_origin = Url::parse(rp_origin_str)
            .map_err(|e| format!("Invalid WebAuthn RP Origin URL: {}", e))?;

        let builder = WebauthnBuilder::new(rp_id, &rp_origin)
            .map_err(|e| format!("WebauthnBuilder failed: {:?}", e))?
            .rp_name("Interview Guide Platform");

        let webauthn = builder
            .build()
            .map_err(|e| format!("Webauthn build failed: {:?}", e))?;

        Ok(Self {
            webauthn: Arc::new(webauthn),
        })
    }

    pub fn start_registration(
        &self,
        user_id: Uuid,
        username: &str,
        display_name: &str,
        exclude_credentials: Option<Vec<CredentialID>>,
    ) -> Result<(CreationChallengeResponse, PasskeyRegistration), String> {
        self.webauthn
            .start_passkey_registration(user_id, username, display_name, exclude_credentials)
            .map_err(|e| format!("Failed to initiate WebAuthn registration: {:?}", e))
    }

    pub fn finish_registration(
        &self,
        reg: &RegisterPublicKeyCredential,
        state: &PasskeyRegistration,
    ) -> Result<Passkey, String> {
        self.webauthn
            .finish_passkey_registration(reg, state)
            .map_err(|e| format!("Failed to verify WebAuthn registration: {:?}", e))
    }

    pub fn start_authentication(
        &self,
        allow_credentials: &[Passkey],
    ) -> Result<(RequestChallengeResponse, PasskeyAuthentication), String> {
        self.webauthn
            .start_passkey_authentication(allow_credentials)
            .map_err(|e| format!("Failed to initiate WebAuthn authentication: {:?}", e))
    }

    pub fn finish_authentication(
        &self,
        auth: &PublicKeyCredential,
        state: &PasskeyAuthentication,
    ) -> Result<AuthenticationResult, String> {
        self.webauthn
            .finish_passkey_authentication(auth, state)
            .map_err(|e| format!("Failed to verify WebAuthn authentication: {:?}", e))
    }
}
