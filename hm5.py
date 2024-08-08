def remove_key_from_dict(dictionary: dict):
    dictionary.popitem()
def clear_all(dictionary: dict):
    dictionary = { }
a = {'x': 1, 'y': 2}
remove_key_from_dict(a)
print(a)
clear_all(a)
print(a)



#כן, המילון שנשלח לפונקציה remove_key_from_dictישתנה. מילון הוא אובייקט הניתן לשינוי ב-Python. כאשר אתה מעביר מילון לפונקציה, אתה מעביר הפניה למילון המקורי, לא עותק. לכן, כל שינוי שנעשה במילון בתוך הפונקציה משפיע על המילון המקורי.
#לא השתנה שהשורה dictionary = {} יוצרת מילון חדש ומבצע רק שינוי על העתק מקומי של המשתנה dictionary, ולא על המילון המקורי שנשלח לפונקציה.

def clear_dict_values(dictionary: dict):
    for key in dictionary:
        dictionary[key].clear()


