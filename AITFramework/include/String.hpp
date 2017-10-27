/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * File:   MyString.h
 * Author: k15125kk
 *
 * Created on 2017/04/14, 11:42
 */

#ifndef MY_STRING_H
#define MY_STRING_H

#include <stddef.h>
#include <cstdlib>
#include <hashtable.h>

namespace ait {

    class String {
    public:
        String();
        String(const char* str);
        String(const String& orig);
        virtual ~String();

        //演算子オーバーロード
        String operator+(const char* str);
        String operator+(const String& str);
        String& operator+=(const char* str);
        String& operator+=(const String& str);
        String& operator=(const char* str);
        String& operator=(const String& str);
        bool operator==(const char* str) const;
        bool operator==(const String& str) const;
        bool operator!=(const char* str) const;
        bool operator!=(const String& str) const;

        //メンバ関数
        const char* getCharPointer(void) const;
        int length(void);
        bool isEmpty(void);
        int hashCode(void) const;

        static String valueOf(int val);
        static String valueOf(unsigned int val);
        static String valueOf(long val);
        static String valueOf(unsigned long val);
        static String valueOf(long long val);
        static String valueOf(unsigned long long val);
        static String valueOf(float val);
        static String valueOf(double val);
        static String valueOf(long double val);
    private:
        size_t m_capacity;
        size_t m_size;
        char* m_data;
    };
}

namespace std{
    template<>
    struct hash<ait::String>{
        std::size_t operator()(const ait::String& key) const{
            return key.hashCode();
        }
    };
}
#endif /* MY_STRING_H */
