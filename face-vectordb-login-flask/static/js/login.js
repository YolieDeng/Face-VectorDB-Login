document.addEventListener('DOMContentLoaded', (event) => {
    const video = document.getElementById('video');
    const startButton = document.getElementById('startBtnLogin');
    const stopButton = document.getElementById('stopBtnLogin');
    const loginButton = document.getElementById('loginButton');
    const canvas_video = document.createElement('canvas');
    let frameDetectionActive = false;

    canvas_video.style.maxWidth = "100%";
    canvas_video.style.maxHeight = "100%";
    canvas_video.style.display = "none";

    // 启动摄像头的函数
    const startCamera = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            // 设置视频流标志为true
            flag = true;
            // 开始监控视频帧
            startFrameDetection(video);
        } catch (error) {
            console.error('Error accessing camera:', error);
        }
    };

    // 停止摄像头的函数
    const stopCamera = () => {
        const stream = video.srcObject;
        const tracks = stream.getTracks();

        tracks.forEach(track => track.stop());
        video.srcObject = null;
        // 设置视频流标志为false，停止视频流的监控
        flag = false;
        frameDetectionActive = false;
    };

    // 实时监测视频帧并发送到服务器
    async function startFrameDetection(preview) {
        frameDetectionActive = true;
        while (flag && frameDetectionActive) {
            canvas_video.width = preview.offsetWidth;
            canvas_video.height = preview.offsetHeight;
            const ctx = canvas_video.getContext('2d');
            ctx.drawImage(preview, 0, 0, preview.videoWidth, preview.videoHeight, 0, 0, canvas_video.width, canvas_video.height);

            // const img_base64 = canvas_video.toDataURL("image/png", 1.0);
            // sendImageToServer(img_base64);
            await new Promise(resolve => requestAnimationFrame(resolve));
            // setTimeout(detect, 0);
        }
    }

    // 发送数据到后端
    const sendImageToServer = (photoDataUrl) => {
        const requestData = {
            "frame": photoDataUrl,
        };

        $.ajax({
            type: 'POST',
            url: '/fvdb/login',
            contentType: 'application/json',
            dataType: 'json',
            data: JSON.stringify(requestData),
            success: function (data) {
                alert(data.message);
            },
            error: function (error) {
                console.error('Error:', error);
            }
        });
    };

    // 点击登录按钮时触发的事件
    loginButton.addEventListener('click', () => {
        const img_base64 = canvas_video.toDataURL("image/png", 1.0);
        sendImageToServer(img_base64);
        // stopFrameDetection();
    });

    // 停止帧检测的函数
    function stopFrameDetection() {
        frameDetectionActive = false;
        console.log('Frame detection stopped');
    }

    startButton.addEventListener('click', () => {
        startCamera();
    });
    stopButton.addEventListener('click', stopCamera);
});
