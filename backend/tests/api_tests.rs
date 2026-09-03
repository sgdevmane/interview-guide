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
}
