#include <windows.h>

extern "C" {

    // 从当前位置平滑移动到 (x, y)，duration 秒 —— 效果同 pyautogui.moveTo
    __declspec(dllexport) void MoveTo(int x, int y, double duration)
    {
        POINT cur;
        GetCursorPos(&cur);
        int steps = (int)(duration * 60);
        if (steps < 1) steps = 1;
        int sleep_ms = (int)(duration * 1000.0 / steps);
        for (int i = 1; i <= steps; i++) {
            double t = (double)i / steps;
            SetCursorPos((int)(cur.x + (x - cur.x) * t),
                (int)(cur.y + (y - cur.y) * t));
            Sleep(sleep_ms);
        }
        SetCursorPos(x, y);
    }

    __declspec(dllexport) void MouseDown()
    {
        mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);
    }

    __declspec(dllexport) void MouseUp()
    {
        mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);
    }

}
