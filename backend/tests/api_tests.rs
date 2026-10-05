#[cfg(test)]
mod tests {
    use std::path::Path;

    #[test]
    fn test_sm2_algorithm_calculations() {
        let q_score: f32 = 4.0;
        let mut ease_factor: f32 = 2.5;
        let _repetitions: u32 = 2;
        let interval_days: u32 = 6;

        ease_factor = ease_factor + (0.1 - (5.0 - q_score) * (0.08 + (5.0 - q_score) * 0.02));
        assert!(ease_factor >= 1.3);

        let next_interval = ((interval_days as f32) * ease_factor).round() as u32;
        assert!(next_interval >= 6);
    }

    #[test]
    fn test_markdown_directory_structure() {
        let md_path = Path::new("../markdowns");
        if md_path.exists() {
            assert!(md_path.is_dir());
        }
    }

    #[test]
    fn test_sm18_spaced_repetition_calculations() {
        let prev_stability: f32 = 4.0;
        let prev_difficulty: f32 = 5.0;
        let grade: u8 = 4;

        let grade_factor = (grade as f32 - 3.0) * 0.1;
        let new_difficulty = (prev_difficulty - grade_factor).clamp(1.0, 10.0);
        let difficulty_mod = 1.0 + (10.0 - new_difficulty) * 0.15;
        let new_stability = prev_stability * (1.2 + grade_factor) * difficulty_mod;
        let optimal_interval_days = ((new_stability * (0.9_f32).ln()) / (0.95_f32).ln()).round().max(1.0) as u32;

        assert!(new_stability > prev_stability);
        assert!(new_difficulty <= prev_difficulty);
        assert!(optimal_interval_days >= 1);
    }

    #[test]
    fn test_certificate_sha256_fingerprint() {
        use sha2::{Digest, Sha256};
        let raw = "Alex Morgan|Staff Distributed Systems Engineer|1840|94.5";
        let mut hasher = Sha256::new();
        hasher.update(raw.as_bytes());
        let hash = format!("{:x}", hasher.finalize());
        assert_eq!(hash.len(), 64);
    }

    #[test]
    fn test_keystroke_entropy_calculation() {
        let intervals = vec![120u32, 95, 110, 85, 140, 90, 80];
        let n = intervals.len() as f64;
        let mean = intervals.iter().copied().sum::<u32>() as f64 / n;
        let variance = intervals.iter().map(|&x| (x as f64 - mean).powi(2)).sum::<f64>() / n;
        let std_dev = variance.sqrt();
        let entropy_score = (std_dev / 50.0).clamp(0.0, 1.0);
        assert!(entropy_score > 0.0 && entropy_score <= 1.0);
        assert!(entropy_score >= 0.35, "Natural typing variance should exceed automated paste threshold");
    }

    #[test]
    fn test_verifiable_credential_structure() {
        let did = "did:key:z6MkhaXgBZDvotDkL5257faiz4898XnpGuvZSD6EDLk81tKA";
        let track = "Staff Distributed Systems Engineer";
        let grade = 95.5f64;
        let payload = format!("{}|{}|{:.2}", did, track, grade);
        assert!(payload.contains("did:key"));
        assert!(grade >= 90.0);
    }
}

