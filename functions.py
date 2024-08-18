def generate_ravdess_csv(dir_list):
  data = []
  for parent_dir in dir_list:
    for root, dirs, files in os.walk(parent_dir):
      for file in files:
        if file.endswith(".wav"):
          filename = file[:-4]  # Remove .wav extension
          parts = filename.split('-')
          modality, vocal_channel, emotion, intensity, statement, repetition, actor = map(int, parts)

        # Determine emotion and intensity label
        emotion_map = {
          1: "neutral",
          2: "calm",
          3: "happy",
          4: "sad",
          5: "angry",
          6: "fearful",
          7: "disgust",
          8: "surprised"
        }
        intensity_map = {
          1: "",
          2: "strongly "
        }
        emotion_label = intensity_map[intensity] + emotion_map[emotion]

        data.append({
            "file_path": os.path.join(root, file),
            "emotion": emotion_label
        })

  # Create DataFrame and return
  df = pd.DataFrame(data)
  return df

if __name__ == "__main__":
  dir_list = ["/content/drive/My Drive/Corpora/RAVDESS/Actor_10", "/content/drive/My Drive/Corpora/RAVDESS/Actor_10"]
  df = generate_ravdess_csv(dir_list)
  df.to_csv("ravdess_data.csv", index=False)

data = pd.read_csv('ravdess_data.csv')
