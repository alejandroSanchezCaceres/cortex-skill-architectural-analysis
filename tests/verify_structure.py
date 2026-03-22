import os

def test_structure():
    root_files = os.listdir('.')
    assert '.gitignore' in root_files, ".gitignore missing from root"
    assert 'README.md' in root_files, "README.md missing from root"
    
    skill_dir = 'cortex-skill-architectural-analysis'
    assert os.path.isdir(skill_dir), "Skill directory missing"
    
    skill_files = os.listdir(skill_dir)
    assert 'SKILL.md' in skill_files, "SKILL.md missing from skill directory"
    assert 'references' in skill_files, "references folder missing from skill directory"
    
    print("Structure verification passed!")

if __name__ == "__main__":
    try:
        test_structure()
    except AssertionError as e:
        print(f"Structure verification failed: {e}")
        exit(1)
