**📄 DeepFace Supported Models**

| Model      | Accuracy (LFW) | Description                                                                 | Weight Size |
|------------|----------------|-----------------------------------------------------------------------------|-------------|
| VGG-Face  | ~98.78%        | One of the earliest deep face recognition models; used as DeepFace default | ~500 MB     |
| Facenet    | ~99.65%        | Google’s model using triplet loss for learning face embeddings              | ~90 MB      |
| Facenet512 | ~99.73%        | A variant of FaceNet with 512-dimensional embeddings                        | ~90 MB      |
| OpenFace   | ~92.92%        | Lightweight model for real-time applications; inspired by FaceNet           | ~90 MB      |
| DeepFace   | ~97.35%        | Facebook’s original deep learning model for face recognition                | ~100 MB     |
| DeepID     | ~97.45%        | Chinese Academy of Sciences model using joint identification-verification   | ~100 MB     |
| ArcFace    | ~99.83%        | SOTA model using additive angular margin loss                               | ~60-100 MB  |
| Dlib       | ~99.38%        | Based on ResNet-34; well optimized for embedding extraction                 | ~100 MB     |
| SFace      | ~99.50%        | Lightweight and fast model for mobile-friendly face recognition             | ~11 MB      |
| GhostFaceNet | ~99.20%      | Efficient and small model designed for edge devices                         | ~15 MB      |
| Buffalo_L  | ~99.85%        | Large version of ArcFace-based model from InsightFace repo                  | ~105 MB     |

---

**🛠️ Model Conversion and Optimization**

| Conversion Method | Description                                                                 | Applicable Models           | Tools / Notes                          |
|-------------------|-----------------------------------------------------------------------------|-----------------------------|----------------------------------------|
| TFLite            | Convert to TensorFlow Lite for mobile deployment                            | All TensorFlow-based models | `tf.lite.TFLiteConverter`              |
| ONNX              | Open Neural Network Exchange format for cross-platform inference            | Most models                 | `tf2onnx`, `keras2onnx`, `pytorch2onnx`|
| Quantization      | Reduce model size/latency by reducing precision (e.g. FP32 → INT8)         | All                         | Post-training / quant-aware training   |
| Pruning           | Remove redundant weights to optimize inference speed                        | TensorFlow, PyTorch models  | TensorFlow Model Optimization Toolkit  |
| CoreML            | Convert to Apple CoreML format for iOS apps                                 | TensorFlow, ONNX            | `coremltools`                          |
| TensorRT          | NVIDIA's inference optimizer for GPU deployment                             | ONNX, TensorFlow            | TensorRT engine builder                |

📌 *Gợi ý*: Với mobile app, bạn nên ưu tiên dùng TFLite + quantization để đạt tốc độ tốt và giảm dung lượng.*

