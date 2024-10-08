import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


def run_food():
    # 한글 폰트 설정 (Windows의 경우 'Malgun Gothic' 사용)
    font_path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    # 파일명
    file_name = '임베디드_음식.xlsx'

    # DataFrame 형식으로 엑셀 파일 읽기
    df = pd.read_excel(file_name)

    # '음식'이라는 열의 데이터 가져오기
    if '음식' in df.columns:
        음식_data = df['음식']

        # 각 항목 카운트
        음식_count = 음식_data.value_counts()

        # 데이터 시각화
        plt.figure(figsize=(8, 6))
        음식_count.plot(kind='bar', color='skyblue')  # 막대 그래프 그리기
        plt.title('음식 빈도수', fontsize=15)
        plt.xlabel('음식 이름', fontsize=12)
        plt.ylabel('빈도', fontsize=12)
        plt.xticks(rotation=45, ha='right')  # 음식 이름 회전
        plt.tight_layout()  # 레이아웃 조정
        plt.show()

        # 머신러닝 모델을 위한 데이터 전처리
        # 음식 데이터를 라벨 인코딩
        label_encoder = LabelEncoder()
        encoded_labels = label_encoder.fit_transform(음식_data)

        # 입력 데이터를 만들기 위해 X, y 분리
        X = encoded_labels.reshape(-1, 1)  # 특성 데이터
        y = encoded_labels  # 라벨 데이터

        # 훈련 세트와 테스트 세트로 분할
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42)

        # 모델 구성
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(10, activation='relu', input_shape=(1,)),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])

        # 모델 컴파일
        model.compile(optimizer='adam',
                      loss='binary_crossentropy', metrics=['accuracy'])

        # 모델 훈련
        model.fit(X_train, y_train, epochs=10, batch_size=1)

        # 모델 평가
        loss, accuracy = model.evaluate(X_test, y_test)
        print(f'모델 정확도: {accuracy * 100:.2f}%')
    else:
        print("'음식'이라는 열이 존재하지 않습니다.")
